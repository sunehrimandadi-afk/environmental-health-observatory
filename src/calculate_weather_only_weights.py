import pandas as pd
import os

# --------------------------------
# Load city-specific weights
# --------------------------------

input_file = (
    "data/processed/model_results/"
    "city_feature_weights.csv"
)

weights_df = pd.read_csv(input_file)


# --------------------------------
# Remove PM2.5 lag feature
# --------------------------------

weather_features = [
    "max_temperature",
    "humidity",
    "wind_speed_10m_max (km/h)",
    "precipitation_sum (mm)",
    "doy_sin",
    "doy_cos"
]


# --------------------------------
# Renormalize weather variables
# --------------------------------

feature_sum = weights_df[weather_features].sum(axis=1)


for feature in weather_features:
    weights_df[feature] = (
        weights_df[feature] / feature_sum
    )


# Remove lag from final output
weather_weights = weights_df[
    ["City"] + weather_features
]


# --------------------------------
# Save
# --------------------------------

output_file = (
    "data/processed/model_results/"
    "weather_only_weights.csv"
)

weather_weights.to_csv(
    output_file,
    index=False
)


print("\nWeather-only risk weights:")
pd.set_option("display.max_columns", None)
print(weather_weights)


print(
    f"\nSaved to {output_file}"
)