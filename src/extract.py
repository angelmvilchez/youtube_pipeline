import os

def extract_data():
    """
    Function for extracting YouTube trending video statistics data from Kaggle.
    Dataset: https://www.kaggle.com/datasets/datasnaek/youtube-new
    """
    print("Reading dataset from Kaggle...")
    os.system("kaggle datasets download -d datasnaek/youtube-new -p ../data/raw --unzip")
    print("Data extracted to data/raw/.")