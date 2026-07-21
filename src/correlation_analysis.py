import pandas as pd
import matplotlib.pyplot as plt
import os


# ==========================
# Paths
# ==========================

DATA_DIR = "data/processed"

OUTPUT_DIR = "data/processed/correlation_results"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ==========================
# City files
# ==========================

city_files = {
    "Houston": "Houston_environment.csv",
    "Los_Angeles": "LA_environment.csv",
    "New_York": "NY_environment.csv",
    "Phoenix": "Phoenix_environment.csv",
    "Sacramento": "Sacramento_environment.csv",
    "Seattle": "Seattle_environment.csv"
}


# ==========================
# Variables
# ==========================

variables = [
    "mean_temperature",
    "humidity",
    "wind_speed_10m_max (km/h)",
    "precipitation_sum (mm)",
    "pm25"
]


# ==========================
# Correlation analysis
# ==========================

for city, file in city_files.items():

    print(f"\nAnalyzing {city}")

    filepath = os.path.join(DATA_DIR, file)

    df = pd.read_csv(filepath)


    # Check columns
    print(df.columns.tolist())


    # Keep available variables
    available_variables = [
        col for col in variables 
        if col in df.columns
    ]


    # Remove missing values
    corr_df = df[available_variables].dropna()


    # Correlation matrix
    corr = corr_df.corr()


    print(corr)


    # Save correlation matrix
    corr.to_csv(
        f"{OUTPUT_DIR}/{city}_correlation_matrix.csv"
    )


    # ==========================
    # Heatmap
    # ==========================

    plt.figure(figsize=(8,6))

    plt.imshow(
        corr,
        aspect="auto"
    )

    plt.colorbar()


    plt.xticks(
        range(len(corr.columns)),
        corr.columns,
        rotation=45,
        ha="right"
    )

    plt.yticks(
        range(len(corr.index)),
        corr.index
    )


    plt.title(
        f"{city} Environmental Correlation"
    )


    plt.tight_layout()


    plt.savefig(
        f"{OUTPUT_DIR}/{city}_correlation_heatmap.png",
        dpi=300
    )


    plt.close()


    # ==========================
    # PM2.5 predictor ranking
    # ==========================

    if "pm25" in corr.columns:

        pm25_rank = (
            corr["pm25"]
            .drop("pm25")
            .sort_values(
                ascending=False
            )
        )

        pm25_rank.to_csv(
            f"{OUTPUT_DIR}/{city}_pm25_predictor_ranking.csv"
        )


print("\nFinished correlation analysis!")