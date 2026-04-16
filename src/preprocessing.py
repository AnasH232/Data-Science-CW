import pandas as pd

from .config import BASE_MODEL_COLUMNS, LEAKAGE_COLUMNS, TARGET_COLUMN

def select_phase3_data(df):
    columns_to_keep = [column for column in BASE_MODEL_COLUMNS if column in df.columns]
    columns_to_drop = [column for column in LEAKAGE_COLUMNS if column in df.columns]
    df_selected = df[columns_to_keep].copy()
    return df_selected, columns_to_keep, columns_to_drop


def filter_phase3_rows(df):
    filtered = df.copy()
    filtered = filtered[filtered["CANCELLED"] == 0]
    filtered = filtered[filtered["DIVERTED"] == 0]
    filtered = filtered.dropna(
        subset=[
            "DEPARTURE_DELAY",
            "SCHEDULED_DEPARTURE",
            "SCHEDULED_TIME",
            "DISTANCE",
            "ORIGIN_AIRPORT",
            "DESTINATION_AIRPORT",
            "AIRLINE",
        ]
    )
    return filtered


def clean_phase3_missing_values(df):
    df_clean = df.copy()

    numeric_columns = df_clean.select_dtypes(include="number").columns.tolist()
    categorical_columns = df_clean.select_dtypes(include=["object"]).columns.tolist()

    for column in numeric_columns:
        if df_clean[column].isna().any():
            df_clean[column] = df_clean[column].fillna(df_clean[column].median())

    for column in categorical_columns:
        if df_clean[column].isna().any():
            mode = df_clean[column].mode(dropna=True)
            fill_value = mode.iloc[0] if not mode.empty else "UNKNOWN"
            df_clean[column] = df_clean[column].fillna(fill_value)

    return df_clean


def drop_duplicate_rows(df):
    before = len(df)
    deduplicated = df.drop_duplicates().copy()
    after = len(deduplicated)
    return deduplicated, before - after


def cap_outliers_iqr(df, columns):
    capped = df.copy()
    summary = {}

    for column in columns:
        if column not in capped.columns:
            continue

        q1 = capped[column].quantile(0.25)
        q3 = capped[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = max((q1 - 1.5 * iqr),0)
        upper_bound = q3 + 1.5 * iqr

        original = capped[column].copy()
        capped[column] = capped[column].clip(lower=lower_bound, upper=upper_bound)
        changed = int((original != capped[column]).sum())

        summary[column] = {
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "capped_values": changed,
        }

    return capped, pd.DataFrame(summary).T if summary else pd.DataFrame()


def add_phase3_features(df):
    enriched = df.copy()
    enriched[TARGET_COLUMN] = (enriched["DEPARTURE_DELAY"] > 15).astype(int)
    enriched["SCHEDULED_DEPARTURE_HOUR"] = (
        enriched["SCHEDULED_DEPARTURE"].floordiv(100).clip(lower=0, upper=23).astype(int)
    )

    return enriched
