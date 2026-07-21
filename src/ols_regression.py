import os
import numpy as np
import pandas as pd
import statsmodels.api as sm

# ==========================
# Settings
# ==========================

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

# ==========================
# Output folder
# ==========================

os.makedirs(
    "data/processed/model_results/ols",
    exist_ok=True
)

# ==========================
# Run OLS for each city
# ==========================

for city in cities:

    print("\n====================================")
    print(f"{city} OLS Regression")
    print("====================================")

    file = f"data/processed/{city}_environment_lagged.csv"

    df = pd.read_csv(file)

    # --------------------------
    # Temporal Features
    # --------------------------

    df["date"] = pd.to_datetime(df["date"])

    df["day_of_year"] = df["date"].dt.dayofyear

    df["doy_sin"] = np.sin(
        2 * np.pi * df["day_of_year"] / 365
    )

    df["doy_cos"] = np.cos(
        2 * np.pi * df["day_of_year"] / 365
    )

    # --------------------------
    # Keep needed columns
    # --------------------------

    data = df[features + [target]].dropna()

    X = data[features]
    y = data[target]

    # --------------------------
    # Fit OLS
    # --------------------------

    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()

    # --------------------------
    # Print Summary
    # --------------------------

    print(model.summary())

    print("\nAdjusted R²:", round(model.rsquared_adj, 3))

    # --------------------------
    # Save coefficient table
    # --------------------------

    results = pd.DataFrame({
        "Coefficient": model.params,
        "Std Error": model.bse,
        "t Statistic": model.tvalues,
        "P-value": model.pvalues,
        "CI Lower": model.conf_int()[0],
        "CI Upper": model.conf_int()[1]
    })

    output = (
        f"data/processed/model_results/ols/"
        f"{city}_ols_results.csv"
    )

    results.to_csv(
        output,
        index=True
    )

    print(f"\nSaved: {output}")

print("\n====================================")
print("Finished OLS analysis for all cities.")
print("====================================")