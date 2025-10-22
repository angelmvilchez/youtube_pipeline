# YouTube videos - ETL pipeline

YouTube trending US video statistics ETL pipeline using Kaggle and Python.

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the [requirements](/requirements.txt).

```bash
pip install -r requirements.txt
```

## Description

This project processes and cleans YouTube US trending video data for storage in a data warehouse, enabling data-driven insights, reports, and visualizations.

The main program is divided into three pieces of code _extract_, _transform_ and _load_ which all can be found in the [src](/src) directory. Each code contains a function and each function is executed in the [main script](/src/main.py).

### Extract
The **extract_data()** function reads the dataset directly from Kaggle.
- Dataset: https://www.kaggle.com/datasets/datasnaek/youtube-new

### Transform
The **transform_data()** function cleans and correctly formats the data, adding value to it by the inclusion of the _like ratio_ column in the dataframe.

### Load
Final phase of the ETL pipeline, the **load_data()** function is in charge of inserting the data into the table _trending_videos_ of the local database (created with SQLite). 

## YouTube US Trending Videos - ETL Pipeline
<img width="711" height="291" alt="YouTube - ETL Pipeline" src="https://github.com/user-attachments/assets/ac8d5ab5-95d5-4456-a5c6-8343de849d6c" />

## Usage

```bash
git clone https://github.com/angelmvilchez/etl_example.git
python src/main.py
```

PD: Remember to authenticate Kaggle for this project.

### Kaggle Authentication Setup

To use the Kaggle API in this project:

1. Go to your Kaggle account → Account → Create New API Token.  
   This downloads a file named `kaggle.json`.

2. Move it to the following location:
   - **Windows:** `C:\Users\<YourUser>\.kaggle\kaggle.json`
   - **Mac/Linux:** `~/.kaggle/kaggle.json`

3. Test it by running:
   ```bash
   kaggle datasets list
   ```

## Results

### Clean data example
Excluding _description_ and _tags_ columns.

<div style="max-height:420px; overflow:auto; border:1px solid #ddd; padding:10px;">

|video_id   |trending_date|title                                                                                                                                                                                                                                                                                                       |channel_title        |category_id|publish_time       |views                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |likes  |dislikes|comment_count|thumbnail_link|comments_disabled                             |ratings_disabled|video_error_or_removed|like_ratio|
|-----------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|-----------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|--------|-------------|--------------|----------------------------------------------|----------------|----------------------|----------|
|2kyS6SvSYSE|11/14/2017   |WE WANT TO TALK ABOUT OUR MARRIAGE                                                                                                                                                                                                                                                                          |CaseyNeistat         |22         |11/13/2017 17:13   |748374                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |57527  |2966    |15954        |https://i.ytimg.com/vi/2kyS6SvSYSE/default.jpg|FALSE                                         |FALSE           |FALSE                 |0.9509695336650521|
|1ZAPwfrtAFY|11/14/2017   |The Trump Presidency: Last Week Tonight with John Oliver (HBO)                                                                                                                                                                                                                                              |LastWeekTonight      |24         |11/13/2017 7:30    |2418783                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |97185  |6146    |12703        |https://i.ytimg.com/vi/1ZAPwfrtAFY/default.jpg|FALSE                                         |FALSE           |FALSE                 |0.9405212375763323|
|5qpjK5DgCt4|11/14/2017   |Racist Superman &#124; Rudy Mancuso, King Bach & Lele Pons                                                                                                                                                                                                                                                       |Rudy Mancuso         |23         |11/12/2017 19:05   |3191434                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |146033 |5339    |8181         |https://i.ytimg.com/vi/5qpjK5DgCt4/default.jpg|FALSE                                         |FALSE           |FALSE                 |0.9647292762201728|
|puqaWrEC7tY|11/14/2017   |Nickelback Lyrics: Real or Fake?                                                                                                                                                                                                                                                                            |Good Mythical Morning|24         |11/13/2017 11:00   |343168                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |10172  |666     |2146         |https://i.ytimg.com/vi/puqaWrEC7tY/default.jpg|FALSE                                         |FALSE           |FALSE                 |0.938549548|


</div>
