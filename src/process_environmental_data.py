import pandas as pd
import os


cities = [
    "Phoenix",
    "LA",
    "Seattle",
    "Houston",
    "NY",
    "Sacramento"
]


raw_folder = "data/raw"
processed_folder = "data/processed"


os.makedirs(processed_folder, exist_ok=True)



for city in cities:

    print(f"\nProcessing {city}...")


    # -------------------------
    # WEATHER
    # -------------------------

    weather_file = f"{raw_folder}/{city}_weather.csv"

    weather = pd.read_csv(
        weather_file,
        skiprows=3
    )

    weather["time"] = pd.to_datetime(weather["time"])

    weather = weather.rename(
        columns={
            "temperature_2m_max (°F)": "max_temperature",
            "temperature_2m_mean (°F)": "mean_temperature",
            "relative_humidity_2m_mean (%)": "humidity"
        }
    )


    weather["date"] = weather["time"].dt.date



    # -------------------------
    # AIR QUALITY
    # -------------------------

    air_file = f"{raw_folder}/{city}_air_quality.csv"

    air = pd.read_csv(
        air_file,
        skiprows=3
    )

    air["time"] = pd.to_datetime(air["time"])


    # hourly → daily average

    air["date"] = air["time"].dt.date


    air_daily = (
        air
        .groupby("date")
        ["pm2_5 (μg/m³)"]
        .mean()
        .reset_index()
    )


    air_daily = air_daily.rename(
        columns={
            "pm2_5 (μg/m³)": "pm25"
        }
    )


    # -------------------------
    # MERGE
    # -------------------------

    combined = weather.merge(
        air_daily,
        on="date",
        how="inner"
    )


    combined["city"] = city


    combined.to_csv(
        f"{processed_folder}/{city}_environment.csv",
        index=False
    )


    print(
        f"{city}: {combined.shape}"
    )


print("\nFinished!")