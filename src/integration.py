from pathlib import Path


def merge_airline_lookup(df, airlines_df):
    merged = df.merge(
        airlines_df.rename(columns={"IATA_CODE": "AIRLINE", "AIRLINE": "AIRLINE_NAME"}),
        on="AIRLINE",
        how="left",
    )
    return merged


def merge_airport_lookup(df, airports_df):
    origin_lookup = airports_df.rename(
        columns={
            "IATA_CODE": "ORIGIN_AIRPORT",
            "AIRPORT": "ORIGIN_AIRPORT_NAME",
            "CITY": "ORIGIN_CITY",
            "STATE": "ORIGIN_STATE",
            "COUNTRY": "ORIGIN_COUNTRY",
            "LATITUDE": "ORIGIN_LATITUDE",
            "LONGITUDE": "ORIGIN_LONGITUDE",
        }
    )
    destination_lookup = airports_df.rename(
        columns={
            "IATA_CODE": "DESTINATION_AIRPORT",
            "AIRPORT": "DESTINATION_AIRPORT_NAME",
            "CITY": "DESTINATION_CITY",
            "STATE": "DESTINATION_STATE",
            "COUNTRY": "DESTINATION_COUNTRY",
            "LATITUDE": "DESTINATION_LATITUDE",
            "LONGITUDE": "DESTINATION_LONGITUDE",
        }
    )

    merged = df.merge(origin_lookup, on="ORIGIN_AIRPORT", how="left")
    merged = merged.merge(destination_lookup, on="DESTINATION_AIRPORT", how="left")
    return merged


def save_prepared_dataset(df, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path
