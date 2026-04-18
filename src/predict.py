from pathlib import Path

import joblib
import pandas as pd


def save_model(model, model_path):
    model_path = Path(model_path)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    return model_path


def load_model(model_path):
    return joblib.load(model_path)


def prepare_prediction_input(records):
    if isinstance(records, dict):
        records = [records]
    return pd.DataFrame(records)


def predict_delay_risk(model, input_records):
    input_df = prepare_prediction_input(input_records)
    predictions = model.predict(input_df)
    probabilities = model.predict_proba(input_df)[:, 1]

    results = input_df.copy()
    results["predicted_delay_15"] = predictions
    results["predicted_delay_probability"] = probabilities
    return results
