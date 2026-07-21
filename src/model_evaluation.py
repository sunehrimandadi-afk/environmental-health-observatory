# ==========================================
# Environmental Health Data Observatory
# Regression Model Comparison + Residual Analysis
# ==========================================


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split


from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


from sklearn.preprocessing import StandardScaler


from scipy.stats import skew, kurtosis


from statsmodels.stats.outliers_influence import variance_inflation_factor



# ==========================================
# Settings
# ==========================================


cities = [
    "Houston",
    "LA",
    "NY",
    "Phoenix",
    "Sacramento",
    "Seattle"
]



target = "pm25"



models = {


    "Weather Only": [

        "max_temperature",
        "humidity",
        "wind_speed_10m_max (km/h)",
        "precipitation_sum (mm)"

    ],


    "Weather + Season": [

        "max_temperature",
        "humidity",
        "wind_speed_10m_max (km/h)",
        "precipitation_sum (mm)",
        "doy_sin",
        "doy_cos"

    ],



    "Weather + Season + Lag": [

        "max_temperature",
        "humidity",
        "wind_speed_10m_max (km/h)",
        "precipitation_sum (mm)",
        "doy_sin",
        "doy_cos",
        "pm25_lag_1"

    ]

}



# Create folders

os.makedirs(
    "data/processed/model_results/vif",
    exist_ok=True
)


os.makedirs(
    "data/processed/model_results/residuals",
    exist_ok=True
)



all_results = []



# ==========================================
# Run Models
# ==========================================


for city in cities:


    print("\n================================")
    print(city)
    print("================================")


    file = (
        f"data/processed/"
        f"{city}_environment_lagged.csv"
    )


    df = pd.read_csv(file)



    # Date processing

    df["date"] = pd.to_datetime(
        df["date"]
    )


    df["day_of_year"] = (
        df["date"]
        .dt
        .dayofyear
    )


    df["doy_sin"] = np.sin(
        2*np.pi*df["day_of_year"]/365
    )


    df["doy_cos"] = np.cos(
        2*np.pi*df["day_of_year"]/365
    )



    print(
        "Rows before cleaning:",
        len(df)
    )



    # ======================================
    # Test each model
    # ======================================


    for model_name, features in models.items():


        print("\nModel:", model_name)



        X = df[features]

        y = df[target]



        data = pd.concat(
            [
                X,
                y
            ],
            axis=1
        ).dropna()



        X = data[features]

        y = data[target]



        print(
            "Rows:",
            len(data)
        )



        # ------------------------------
        # VIF
        # ------------------------------


        if model_name == "Weather + Season + Lag":


            vif = pd.DataFrame()

            vif["Feature"] = X.columns


            vif["VIF"] = [

                variance_inflation_factor(
                    X.values,
                    i
                )

                for i in range(
                    X.shape[1]
                )

            ]


            vif.to_csv(

                f"data/processed/model_results/vif/{city}_vif.csv",

                index=False

            )



        # ------------------------------
        # Train/Test Split
        # ------------------------------


        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.2,

            random_state=42

        )



        model = LinearRegression()



        model.fit(

            X_train,

            y_train

        )



        predictions = model.predict(
            X_test
        )



        # ------------------------------
        # Metrics
        # ------------------------------


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



        print(
            "R²:",
            round(r2,3)
        )

        print(
            "RMSE:",
            round(rmse,3)
        )



        all_results.append({

            "City": city,

            "Model": model_name,

            "R2": r2,

            "RMSE": rmse,

            "MAE": mae,

            "Rows": len(data)

        })



        # ======================================
        # Residual Analysis (only best model)
        # ======================================


        if model_name == "Weather + Season + Lag":



            residuals = (
                y_test -
                predictions
            )



            print("\nResidual Stats")

            print(
                "Mean:",
                residuals.mean()
            )

            print(
                "Std:",
                residuals.std()
            )

            print(
                "Skew:",
                skew(residuals)
            )

            print(
                "Kurtosis:",
                kurtosis(residuals)
            )



            # Predicted vs Actual


            plt.figure(
                figsize=(7,5)
            )


            plt.scatter(
                y_test,
                predictions,
                alpha=0.5
            )


            plt.xlabel(
                "Actual PM2.5"
            )

            plt.ylabel(
                "Predicted PM2.5"
            )


            plt.title(
                f"{city}: Predicted vs Actual"
            )


            plt.plot(
                [
                    y_test.min(),
                    y_test.max()
                ],

                [
                    y_test.min(),
                    y_test.max()
                ]
            )


            plt.savefig(

                f"data/processed/model_results/residuals/{city}_predicted_actual.png",

                dpi=300

            )


            plt.close()



            # Residual vs Prediction


            plt.figure(
                figsize=(7,5)
            )


            plt.scatter(
                predictions,
                residuals,
                alpha=0.5
            )


            plt.axhline(0)


            plt.xlabel(
                "Predicted PM2.5"
            )


            plt.ylabel(
                "Residual"
            )


            plt.title(
                f"{city}: Residual vs Predicted"
            )


            plt.savefig(

                f"data/processed/model_results/residuals/{city}_residual_predicted.png",

                dpi=300

            )


            plt.close()



            # Histogram


            plt.figure(
                figsize=(7,5)
            )


            plt.hist(
                residuals,
                bins=30
            )


            plt.xlabel(
                "Residual"
            )


            plt.ylabel(
                "Frequency"
            )


            plt.title(
                f"{city}: Residual Distribution"
            )


            plt.savefig(

                f"data/processed/model_results/residuals/{city}_residual_histogram.png",

                dpi=300

            )


            plt.close()





# ==========================================
# Save Final Results
# ==========================================


results = pd.DataFrame(
    all_results
)


results = results.sort_values(
    by="R2",
    ascending=False
)



results.to_csv(

    "data/processed/model_results/regression_comparison.csv",

    index=False

)



print("\n================================")
print("DONE")
print("================================")


print(results)