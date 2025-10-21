from datetime import datetime as dt

from extract import extract_data
from transform import transform_data

if __name__ == "__main__":
    print("Script started:", dt.now())
    extract_data()
    transform_data()
    print("Script finished:", dt.now())