import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error


# Load data
file = "data/processed/Phoenix_environment.csv"
df = pd.read_csv(file)

# Check columns
print(df.columns)

# Check missing values
print(df.isnull().sum())

print("Rows before cleaning:", len(df))


# Select features
X = df[
    [
        "max_temperature",
        "humidity",
        "wind_speed_10m_max (km/h)",
        "precipitation_sum (mm)"
    ]
]

# Target
y = df["pm25"]


# Remove rows where model variables are missing
data = pd.concat([X, y], axis=1).dropna()

print("Rows after cleaning:", len(data))


# Split cleaned data back into X and y
X = data.drop(columns=["pm25"])
y = data["pm25"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train model
model = LinearRegression()
model.fit(X_train, y_train)


# Beta coefficients
print("\nCoefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(feature, ":", coef)

print("Intercept:", model.intercept_)


# Predictions
predictions = model.predict(X_test)


# Evaluation
print("\nModel Evaluation")
print("R²:", r2_score(y_test, predictions))
print("MAE:", mean_absolute_error(y_test, predictions))

from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_results = pd.DataFrame()

vif_results["Feature"] = X.columns

vif_results["VIF"] = [
    variance_inflation_factor(X.values, i)
    for i in range(X.shape[1])
]

print("\nVIF Results:")
print(vif_results)

# OLS regression for statistical analysis

X_ols = sm.add_constant(X)

ols_model = sm.OLS(y, X_ols).fit()

print("\nOLS Regression Results:")
print(ols_model.summary())
