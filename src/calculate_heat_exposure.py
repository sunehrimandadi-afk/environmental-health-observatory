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


def heat_index(temp_f, humidity):

    """
    NOAA Heat Index Approximation
    """

    HI = (
        -42.379
        + 2.04901523 * temp_f
        + 10.14333127 * humidity
        - 0.22475541 * temp_f * humidity
        - 0.00683783 * temp_f**2
        - 0.05481717 * humidity**2
        + 0.00122874 * temp_f**2 * humidity
        + 0.00085282 * temp_f * humidity**2
        - 0.00000199 * temp_f**2 * humidity**2
    )

    return HI



for city in cities:

    print(f"Processing {city}")

    file = (
        f"data/processed/"
        f"{city}_environment.csv"
    )

    df = pd.read_csv(file)


    df["date"] = pd.to_datetime(df["date"])


    # -------------------------
    # Heat Index
    # -------------------------

    df["heat_index"] = heat_index(
        df["max_temperature"],
        df["humidity"]
    )

    df["heat_index"] = np.where(
    df["max_temperature"] < 80,
    df["max_temperature"],
    df["heat_index"]
    )


    # -------------------------
    # Z-score
    # -------------------------

    df["heat_z"] = (
        df["heat_index"]
        -
        df["heat_index"].mean()
    ) / df["heat_index"].std()


    # -------------------------
    # Normalize 0-100
    # -------------------------

    df["Heat_Risk"] = (

        (
            df["heat_z"]
            -
            df["heat_z"].min()
        )

        /

        (
            df["heat_z"].max()
            -
            df["heat_z"].min()
        )

    ) * 100



    output = pd.DataFrame({

        "date": df["date"],

        "City": city,

        "temperature":
            df["max_temperature"],

        "humidity":
            df["humidity"],

        "heat_index":
            df["heat_index"],

        "Heat_Risk":
            df["Heat_Risk"]

    })


    results.append(output)



final = pd.concat(results)


final.to_csv(
    "data/processed/model_results/heat_risk.csv",
    index=False
)


print("Saved heat risk.")
