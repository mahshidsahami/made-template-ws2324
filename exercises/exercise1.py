from sqlalchemy import create_engine, String, Float, DECIMAL, INTEGER
import pandas as pd


# Read the CSV file
url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
data = pd.read_csv(url)

# Create a connection to the database
eng = create_engine('sqlite:///airports.sqlite')

# Write the data to the database
data.to_sql('airports', eng, if_exists='replace', index=False, dtype={
    'column_1': INTEGER,
    'column_2': String,
    'column_3': String,
    'column_4': String,
    'column_5': String,
    'column_6': String,
    'column_7': Float,
    'column_8': Float,
    'column_9': INTEGER,
    'column_10': Float,
    'column_11': String,
    'column_12': String,
    'geo_punkt': DECIMAL
})

