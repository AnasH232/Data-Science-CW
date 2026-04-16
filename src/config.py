from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw" / "archive"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

FLIGHTS_PATH = RAW_DATA_DIR / "flights.csv"
AIRLINES_PATH = RAW_DATA_DIR / "airlines.csv"
AIRPORTS_PATH = RAW_DATA_DIR / "airports.csv"
PREPARED_DATA_PATH = PROCESSED_DATA_DIR / "flights_prepared_phase3.csv"

TARGET_COLUMN = "DELAY_15"

BASE_MODEL_COLUMNS = [
    "YEAR",
    "MONTH",
    "DAY",
    "DAY_OF_WEEK",
    "AIRLINE",
    "FLIGHT_NUMBER",
    "ORIGIN_AIRPORT",
    "DESTINATION_AIRPORT",
    "SCHEDULED_DEPARTURE",
    "SCHEDULED_TIME",
    "DISTANCE",
    "DEPARTURE_DELAY",
    "CANCELLED",
    "DIVERTED",
]

LEAKAGE_COLUMNS = [
    "DEPARTURE_TIME",
    "TAXI_OUT",
    "WHEELS_OFF",
    "ELAPSED_TIME",
    "AIR_TIME",
    "WHEELS_ON",
    "TAXI_IN",
    "ARRIVAL_TIME",
    "ARRIVAL_DELAY",
    "ARRIVAL_DELAY_NEW",
    "AIR_SYSTEM_DELAY",
    "SECURITY_DELAY",
    "AIRLINE_DELAY",
    "LATE_AIRCRAFT_DELAY",
    "WEATHER_DELAY",
    "CANCELLATION_REASON",
]
