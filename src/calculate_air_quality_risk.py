import pandas as pd
import numpy as np
import os


cities = [
    "Houston",
    "LA",
    "NY",
    "Phoenix",
    "Sacramento",
    "Seattle"
]


results = []


# -------------------------
# AQI Calculation Function
# -------------------------

def calculate_aqi(pm25):
    """
    Converts PM2.5 concentration to AQI approximation.
    Returns NaN if PM2.5 is missing.
    """

    if pd.isna(pm25):
        return np.nan


    # PM2.5 AQI breakpoints
    if pm25 <= 12.0:
        return (50 / 12.0) * pm25

    elif pm25 <= 35.4:
        return (
            (100 - 51) /
            (35.4 - 12.1)
        ) * (pm25 - 12.1) + 51


    elif pm25 <= 55.4:
        return (
            (150 - 101) /
            (55.4 - 35.5)
        ) * (pm25 - 35.5) + 101


    elif pm25 <= 150.4:
        return (
            (200 - 151) /
            (150.4 - 55.5)
        ) * (pm25 - 55.5) + 151


    else:
        return 300



for city in cities:

    print(f"Processing {city}")


    file = (
        f"data/processed/"
        f"{city}_environment.csv"
    )


    df = pd.read_csv(file)


    df["date"] = pd.to_datetime(
        df["date"]
    )


    # -------------------------
    # Remove missing PM2.5
    # -------------------------

    df = df.dropna(
        subset=["pm25"]
    )


    # -------------------------
    # Calculate AQI
    # -------------------------

    df["AQI"] = df["pm25"].apply(
        calculate_aqi
    )


    # -------------------------
    # Normalize AQI Risk 0-100
    # -------------------------

    df["Air_Quality_Risk"] = (

        (
            df["AQI"]
            -
            df["AQI"].min()
        )

        /

        (
            df["AQI"].max()
            -
            df["AQI"].min()
        )

    ) * 100



    output = pd.DataFrame({

        "date": df["date"],

        "City": city,

        "pm25": df["pm25"],

        "AQI": df["AQI"],

        "Air_Quality_Risk":
            df["Air_Quality_Risk"]

    })


    results.append(output)



final = pd.concat(results)


os.makedirs(
    "data/processed/model_results",
    exist_ok=True
)


final.to_csv(
    "data/processed/model_results/air_quality_risk.csv",
    index=False
)


print(final.head())

print("\nMissing values:")
print(final.isna().sum())


print(
    "\nSaved air quality risk."
)