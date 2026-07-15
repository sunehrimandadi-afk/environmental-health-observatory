import pandas as pd
import glob
import os


# Location of raw data
data_folder = "data/raw/"


# Find all CSV files
files = glob.glob(data_folder + "*.csv")


print("Files found:")
for file in files:
    print(file)

print("\n" + "="*60)


# Check every file
for file in files:

    filename = os.path.basename(file)

    print(f"\nDATASET: {filename}")
    print("-"*60)


    # Open-Meteo weather files have metadata rows
    if "weather" in filename.lower():

        df = pd.read_csv(
            file,
            skiprows=3,
            header=0
        )

    else:

        # Air quality files
        df = pd.read_csv(
            file,
            skiprows=3,
            header=0
        )


    # Basic information

    print("Shape:")
    print(df.shape)


    print("\nColumns:")
    print(list(df.columns))


    print("\nData Types:")
    print(df.dtypes)


    print("\nMissing Values:")
    print(df.isnull().sum())


    print("\nDuplicate Rows:")
    print(df.duplicated().sum())


    # Date information

    possible_dates = [
        col for col in df.columns
        if "date" in col.lower()
        or "time" in col.lower()
    ]


    if len(possible_dates) > 0:

        date_column = possible_dates[0]

        print("\nDate Range:")

        print("Start:",
              df[date_column].min())

        print("End:",
              df[date_column].max())


    print("\nSummary Statistics:")
    print(df.describe())


    print("="*60)