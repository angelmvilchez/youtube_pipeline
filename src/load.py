import pandas as pd
from sqlalchemy import create_engine

def load_data():
    """
    Function for loading cleaned data to local SQLite database.
    """
    engine = create_engine("sqlite:///../database/youtube_pipeline.db")
    df = pd.read_csv("../data/clean/youtube_trending_clean.csv")
    print("Loading data to 'trending_videos' table...")
    df.to_sql("trending_videos", con=engine, if_exists="replace", index=False)
    print("Data loaded into SQLite database.")