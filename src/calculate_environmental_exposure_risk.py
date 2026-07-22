import pandas as pd


heat = pd.read_csv(
    "data/processed/model_results/heat_risk.csv"
)


air = pd.read_csv(
    "data/processed/model_results/air_quality_risk.csv"
)


heat["date"] = pd.to_datetime(
    heat["date"]
)

air["date"] = pd.to_datetime(
    air["date"]
)


# Merge

df = heat.merge(
    air,
    on=[
        "date",
        "City"
    ],
    how="inner"
)


# Remove incomplete rows

df = df.dropna(
    subset=[
        "Heat_Risk",
        "Air_Quality_Risk"
    ]
)



# Environmental Risk

df["Environmental_Exposure_Risk"] = (

    0.5 * df["Heat_Risk"]

    +

    0.5 * df["Air_Quality_Risk"]

)



df.to_csv(
    "data/processed/model_results/environmental_health_risk.csv",
    index=False
)


print(df.head())

print("\nMissing values:")
print(df.isna().sum())


print(
    "\nSaved environmental health risk."
)