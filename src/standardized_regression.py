import os
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# ----------------------------
# Settings
# ----------------------------

cities = [
    "Houston",
    "LA",
    "NY",
    "Phoenix",
    "Sacramento",
    "Seattle"
]

features = [
    "max_temperature",
    "humidity",
    "wind_speed_10m_max (km/h)",
    "precipitation_sum (mm)",
    "doy_sin",
    "doy_cos",
    "pm25_lag_1"
]

target = "pm25"

results = []

# ----------------------------
# Standardized Regression
# ----------------------------

for city in cities:

    print(f"\n{'='*40}")
    print(city)
    print("="*40)

    file = f"data/processed/{city}_environment_lagged.csv"

    df = pd.read_csv(file)

    df["date"] = pd.to_datetime(df["date"])

    df["day_of_year"] = df["date"].dt.dayofyear

    df["doy_sin"] = np.sin(
        2*np.pi*df["day_of_year"]/365
    )

    df["doy_cos"] = np.cos(
        2*np.pi*df["day_of_year"]/365
    )

    X = df[features]
    y = df[target]

    data = pd.concat([X,y],axis=1).dropna()

    X = data[features]
    y = data[target]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    model = LinearRegression()

    model.fit(X_scaled,y)

    print("\nStandardized Coefficients")

    row = {"City":city}

    for feature,coef in zip(features,model.coef_):

        row[feature] = coef

        print(
            feature,
            ":",
            round(coef,4)
        )

    results.append(row)

# ----------------------------
# Save coefficients
# ----------------------------

coef_df = pd.DataFrame(results)

os.makedirs(
    "data/processed/model_results",
    exist_ok=True
)

coef_df.to_csv(
    "data/processed/model_results/standardized_coefficients.csv",
    index=False
)

print("\nSaved standardized coefficients.")