# Model Design

## Modeling Goal

The goal of this project is to quantify relationships between environmental conditions and create an environmental health risk indicator.

---

## Variables

### Predictor Variables (Inputs)

| Variable | Purpose |
|---|---|
| Temperature | Measures heat exposure |
| PM2.5 | Measures air pollution |
| Humidity | Represents weather conditions |
| Wind Speed | Represents pollutant movement |
| Precipitation | Represents rainfall effects on environmental conditions |
| City | Allows comparison between locations |

---

## Model 1: PM2.5 Prediction

The first model will examine whether weather conditions can explain changes in PM2.5 levels.

Formula:

PM2.5 = f(Temperature, Humidity, Wind Speed)

Purpose:

Determine how environmental conditions influence pollution levels.

---

## Model 2: Environmental Risk Score

A risk score will combine heat and pollution exposure.

Heat Score:

Temperature values will be normalized between 0 and 1.

PM2.5 Score:

PM2.5 values will be normalized between 0 and 1.

Initial Risk Score:

Risk Score = 0.5(Heat Score) + 0.5(PM2.5 Score)

The weights may be adjusted later based on statistical analysis.

---

## Analysis Steps

1. Clean environmental data.
2. Explore trends and patterns.
3. Calculate correlations between variables.
4. Build regression models.
5. Calculate environmental risk scores.
6. Visualize results.

---

## Model Evaluation

Models will be evaluated using:

- R²: Measures how well the model explains variation.
- RMSE: Measures prediction error.
- Residual analysis: Checks model accuracy.