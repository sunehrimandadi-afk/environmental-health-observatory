import pandas as pd
import os


cities = [
    "Houston",
    "LA",
    "NY",
    "Phoenix",
    "Sacramento",
    "Seattle"
]


for city in cities:

    print("======================")
    print(city)
    print("======================")


    file = f"data/processed/{city}_environment.csv"


    df = pd.read_csv(file)


    # Convert date
    df["date"] = pd.to_datetime(df["date"])


    # Sort chronologically
    df = df.sort_values("date")


    # Add lag features
    df["pm25_lag_1"] = (
        df["pm25"]
        .shift(1)
    )


    # Rolling averages
    df["pm25_rolling_3"] = (
        df["pm25"]
        .shift(1)
        .rolling(window=3)
        .mean()
    )


    df["pm25_rolling_7"] = (
        df["pm25"]
        .shift(1)
        .rolling(window=7)
        .mean()
    )


    # Save updated file
    output = (
        f"data/processed/{city}_environment_lagged.csv"
    )


    df.to_csv(
        output,
        index=False
    )


    print("Saved:", output)