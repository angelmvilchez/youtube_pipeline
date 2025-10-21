import glob
import pandas as pd

def transform_data():
    """
    Function for cleaning and transforming US videos statistics data.
    """
    files = glob.glob("../data/raw/*.csv")
    print(f"Total files ({len(files)}):")
    print(files)
    for f in files:
        if f.endswith(("USvideos.csv")):
            print("Reading 'USvideos.csv'...")
            df = pd.read_csv(f)
            print("Dataframe:")
            break
    
    # View dataframe
    print(df)
    print(df.info())

    print("Date columns not formatted:")
    print(df[["trending_date", "publish_time"]])

    # Clean and format
    print("Cleaning and formatting data...")
    df = df.drop_duplicates(subset=["video_id"])
    df["title"] = df["title"].str.strip()
    df["trending_date"] = pd.to_datetime(df["trending_date"], format="%y.%d.%m")
    df["publish_time"] = pd.to_datetime(df["publish_time"], format="%Y-%m-%dT%H:%M:%S.%fZ")

    print("Date columns formatted correctly:")
    print(df[["trending_date", "publish_time"]])

    # Likes / Total (likes + dislikes)
    print("Adding 'like_ratio' column...") 
    df["like_ratio"] = df["likes"] / (df["likes"] + df["dislikes"]).replace(0, 1)

    print("Writing transformed data to 'data/clean/'...")
    df.to_csv("../data/clean/youtube_trending_clean.csv", index=False)
    print("Data transformed and saved to data/clean/.")