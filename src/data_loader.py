import pandas as pd

from .config import AIRLINES_PATH, AIRPORTS_PATH, FLIGHTS_PATH


def load_flights(path=FLIGHTS_PATH, **read_csv_kwargs):
    options = {"low_memory": False}
    options.update(read_csv_kwargs)
    return pd.read_csv(path, **options)


def load_airlines(path=AIRLINES_PATH, **read_csv_kwargs):
    return pd.read_csv(path, **read_csv_kwargs)


def load_airports(path=AIRPORTS_PATH, **read_csv_kwargs):
    return pd.read_csv(path, **read_csv_kwargs)
