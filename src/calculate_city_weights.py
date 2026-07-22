import pandas as pd
import os

# -----------------------------
# Load standardized coefficients
# -----------------------------

input_file = (
    "data/processed/model_results/"
    "standardized_coefficients.csv"
)

coef_df = pd.read_csv(input_file)


# -----------------------------
# Features to convert into weights
# -----------------------------

features = [
    "max_temperature",
    "humidity",
    "wind_speed_10m_max (km/h)",
    "precipitation_sum (mm)",
    "doy_sin",
    "doy_cos",
    "pm25_lag_1"
]


# -----------------------------
# Calculate city-specific weights
# -----------------------------

weights_df = coef_df[["City"]].copy()


for feature in features:
    
    # absolute standardized coefficient
    weights_df[feature] = coef_df[feature].abs()


# normalize within each city
feature_sum = weights_df[features].sum(axis=1)


for feature in features:
    
    weights_df[feature] = (
        weights_df[feature] / feature_sum
    )


# -----------------------------
# Save results
# -----------------------------

output_dir = (
    "data/processed/model_results"
)

os.makedirs(
    output_dir,
    exist_ok=True
)


output_file = (
    f"{output_dir}/city_feature_weights.csv"
)


weights_df.to_csv(
    output_file,
    index=False
)


print("\nCity-specific feature weights:")
pd.set_option("display.max_columns", None)
print(weights_df)


print(
    f"\nSaved to {output_file}"
)