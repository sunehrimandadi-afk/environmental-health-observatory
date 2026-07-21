import sqlite3
import pandas as pd
import numpy as np


# ==========================
# Connect to database
# ==========================

conn = sqlite3.connect(
    "data/environmental_health.db"
)


# ==========================
# Load table
# ==========================

df = pd.read_sql(
    """
    SELECT *
    FROM environmental_daily
    """,
    conn
)


print("Original columns:")
print(df.columns)



# ==========================
# Create seasonal features
# ==========================

df["date"] = pd.to_datetime(
    df["date"]
)


df["day_of_year"] = (
    df["date"]
    .dt
    .dayofyear
)


# Cyclical encoding

df["doy_sin"] = np.sin(
    2 * np.pi * df["day_of_year"] / 365
)


df["doy_cos"] = np.cos(
    2 * np.pi * df["day_of_year"] / 365
)



# ==========================
# Create PM2.5 lag feature
# ==========================

df = df.sort_values(
    ["city", "date"]
)


df["pm25_lag_1"] = (
    df.groupby("city")["pm25"]
    .shift(1)
)



# Remove first day of each city
df = df.dropna()



# ==========================
# Replace database table
# ==========================

df.to_sql(
    "environmental_daily",
    conn,
    if_exists="replace",
    index=False
)


conn.close()


print("\nDatabase updated successfully!")
print(df.head())
print(df.columns)