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

Daily temperature values will be transformed using z-score standardization:

z = (x - mean) / standard deviation

Higher positive z-scores indicate temperatures that are unusually high compared to typical conditions.

### PM2.5 Score

Daily PM2.5 concentrations will also be transformed using z-score standardization.

Higher positive z-scores indicate unusually high pollution levels.

### Initial Risk Score

The initial environmental risk score will combine heat and pollution exposure:

Risk Score = 0.5(Heat z-score) + 0.5(PM2.5 z-score)

Equal weights are used as a baseline assumption. These weights may be modified later based on statistical analysis and model results.
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