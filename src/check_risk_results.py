import pandas as pd


df = pd.read_csv(
    "data/processed/model_results/environmental_health_risk.csv"
)


print("\nFirst rows:")
print(df.head())


print("\nMissing values:")
print(df.isna().sum())


print(
    df.sort_values(
        "Environmental_Exposure_Risk",
        ascending=False
    )
    .head(10)[
        [
            "date",
            "City",
            "temperature",
            "humidity",
            "heat_index",
            "Heat_Risk",
            "pm25",
            "AQI",
            "Air_Quality_Risk",
            "Environmental_Exposure_Risk"
        ]
    ]
)