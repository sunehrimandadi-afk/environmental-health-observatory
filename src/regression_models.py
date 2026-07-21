import pandas as pd
import numpy as np
import os

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

from statsmodels.stats.outliers_influence import variance_inflation_factor
import os


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


results = []


# ==========================
# Run regression for cities
# ==========================

for city in cities:

    print("\n==========================")
    print(f"{city} Regression Model")
    print("==========================")


    file = f"data/processed/{city}_environment_lagged.csv"

    df = pd.read_csv(file)

    # ==========================
    # Add temporal features
    # ==========================

    df["date"] = pd.to_datetime(df["date"])

    # Extract day of year
    df["day_of_year"] = df["date"].dt.dayofyear

    # Encode yearly seasonal cycle
    df["doy_sin"] = np.sin(
    2 * np.pi * df["day_of_year"] / 365
    )

    df["doy_cos"] = np.cos(
    2 * np.pi * df["day_of_year"] / 365
    )


    print("Rows before cleaning:", len(df))


    # Select variables
    X = df[features]
    y = df[target]


    # Remove missing data
    data = pd.concat(
        [X, y],
        axis=1
    ).dropna()


    X = data[features]
    y = data[target]


    print("Rows after cleaning:", len(data))

    # ==========================
    # VIF Analysis
    # ==========================

    vif_results = pd.DataFrame()

    vif_results["Feature"] = X.columns

    vif_results["VIF"] = [
        variance_inflation_factor(
            X.values,
            i
        )
        for i in range(X.shape[1])
    ]

    print("\nVIF Results:")
    print(vif_results)


    os.makedirs(
        "data/processed/model_results/vif",
        exist_ok=True
    )

    vif_results.to_csv(
        f"data/processed/model_results/vif/{city}_vif.csv",
        index=False
    )


    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


    # Train model
    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )


    # Predictions
    predictions = model.predict(X_test)


    # ==========================
    # Evaluation Metrics
    # ==========================

    r2 = r2_score(
        y_test,
        predictions
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions
        )
    )


    print("\nEvaluation:")
    print("R²:", round(r2, 3))
    print("MAE:", round(mae, 3))
    print("RMSE:", round(rmse, 3))


    # ==========================
    # Coefficients
    # ==========================

    print("\nCoefficients:")

    for feature, coef in zip(
        features,
        model.coef_
    ):
        print(
            feature,
            ":",
            round(coef, 4)
        )


    # Save results
    results.append(
        {
            "City": city,
            "R2": r2,
            "RMSE": rmse,
            "MAE": mae,
            "Rows Used": len(data)
        }
    )


# ==========================
# Save comparison table
# ==========================

results_df = pd.DataFrame(results)


results_df = results_df.sort_values(
    by="R2",
    ascending=False
)


os.makedirs(
    "data/processed/model_results",
    exist_ok=True
)


results_df.to_csv(
    "data/processed/model_results/regression_comparison.csv",
    index=False
)


print("\n==========================")
print("Final Model Comparison")
print("==========================")

print(results_df)


print("\nSaved:")
print(
    "data/processed/model_results/weather_season_regression_comparison.csv"
)
