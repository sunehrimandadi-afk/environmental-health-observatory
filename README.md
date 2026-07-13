# Environmental Health Data Observatory  
## Heat, PM2.5, and Environmental Health Risk Modeling

## Overview

The **Environmental Health Data Observatory** is a data science project that investigates how extreme temperatures and PM2.5 concentrations vary across U.S. cities and how statistical models can quantify environmental health risk.

This project uses environmental data from the **Open-Meteo API** to analyze the relationship between **extreme heat exposure** and **PM2.5 air pollution concentrations**.

The goal is to develop an **environmental exposure risk indicator** that identifies periods and locations with elevated environmental conditions. This project does not predict individual health outcomes; instead, it studies environmental exposure patterns using statistical modeling.

---

# Research Question

**How can statistical models quantify and predict environmental health risk by analyzing the relationship between extreme temperatures and PM2.5 concentrations across U.S. cities?**

---

# Objectives

This project aims to:

1. Collect temperature and PM2.5 data from the Open-Meteo API.
2. Analyze relationships between extreme temperatures and PM2.5 concentrations.
3. Use correlation analysis to identify relationships between environmental variables.
4. Build regression models to quantify how temperature and weather conditions influence PM2.5 levels.
5. Develop an environmental risk score combining heat exposure and PM2.5 concentrations.
6. Create an interactive dashboard to visualize environmental risk patterns.

---

# Scientific Motivation

Extreme heat and air pollution are important environmental exposure factors.

High temperatures can increase heat stress and influence atmospheric conditions that affect pollutant formation and concentration. PM2.5 is an important air quality indicator because fine particulate matter can remain suspended in the atmosphere and represent increased pollution exposure.

By analyzing temperature and PM2.5 together, this project investigates how environmental conditions contribute to differences in exposure risk across U.S. cities.

---

# Study Locations

The project analyzes six U.S. cities representing different climate patterns and environmental conditions.

| City | Reason for Inclusion |
|---|---|
| Phoenix, AZ | Extreme desert heat |
| Sacramento, CA | Hot inland climate and wildfire smoke exposure |
| Los Angeles, CA | Urban heat and pollution patterns |
| Seattle, WA | Cooler climate comparison |
| Houston, TX | Heat and humidity conditions |
| New York, NY | Dense urban environment and seasonal variation |

---

# Data Source

## Open-Meteo API

This project uses the Open-Meteo API to collect daily weather and air quality data.

---

# Variables Collected

| Variable | Description | Purpose |
|---|---|---|
| date | Date of observation | Time tracking |
| city | Location | Compare regions |
| latitude | Geographic coordinate | Location reference |
| longitude | Geographic coordinate | Location reference |
| temperature_max | Daily maximum temperature | Measure extreme heat exposure |
| temperature_mean | Average daily temperature | Measure average heat exposure |
| humidity | Relative humidity | Environmental condition |
| wind_speed | Wind conditions | Pollution dispersion |
| precipitation | Daily precipitation | Weather condition |
| PM2.5 | Fine particulate matter concentration | Measure air pollution exposure |

---

# Statistical Analysis Plan

## 1. Correlation Analysis

Correlation analysis will examine whether temperature and PM2.5 concentrations change together.

Example:

\[
r = correlation(Temperature, PM2.5)
\]

Questions:

- Are hotter days associated with higher PM2.5 concentrations?
- Do relationships differ between cities?

Correlation will be used to identify patterns between environmental variables.

---

# 2. Regression Modeling

Regression analysis will quantify how environmental variables contribute to PM2.5 concentrations.

A possible model:

\[
PM2.5 = \beta_0+\beta_1(Temperature)+\beta_2(Humidity)+\beta_3(Wind)+\epsilon
\]

Where:

- PM2.5 = predicted pollution concentration
- Temperature = heat exposure
- Humidity = atmospheric conditions
- Wind = pollutant movement conditions
- β values = estimated contribution of each variable
- ε = unexplained variation

Model evaluation will include:

- R²
- RMSE
- Residual analysis

---

# Environmental Risk Score

An environmental risk indicator will be created by combining heat exposure and PM2.5 concentration.

Initial baseline:

\[
Environmental\ Risk =
0.5(HeatScore)+0.5(PM2.5Score)
\]

Where:

- HeatScore represents relative temperature exposure.
- PM2.5Score represents relative pollution exposure.

The initial equal weighting provides a transparent baseline. Future analysis may modify weights using statistical results from regression models.

The risk score represents environmental exposure conditions and does not directly predict individual health outcomes.

---

# Dashboard

The final project will include an interactive dashboard displaying:

- Temperature patterns
- PM2.5 concentration trends
- City comparisons
- Environmental risk score patterns
- High-risk environmental days

Tools:

- Streamlit
- Plotly

---

# Technologies

## Programming

- Python

## Data Analysis

- Pandas
- NumPy
- SciPy
- Scikit-learn

## Visualization

- Matplotlib
- Plotly
- Streamlit

## Development Tools

- Git
- GitHub
- Jupyter Notebook
- VS Code

---

# Repository Structure
environmental-health-observatory/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│
├── src/
│
├── dashboard/
│
├── docs/
│ ├── background_research.md
│ ├── study_design.md
│ ├── model_design.md
│ └── data_dictionary.md
│
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

---

# Documentation

## background_research.md

Scientific background on:

- Extreme heat
- PM2.5
- Environmental health relationships
- Statistical concepts

## study_design.md

Contains:

- Research question
- Selected cities
- Variables
- Data collection plan

## model_design.md

Explains:

- Statistical models
- Predictor variables
- Regression approach
- Model evaluation

## data_dictionary.md

Contains:

- Dataset variables
- Data types
- Variable descriptions

---

# Future Improvements

Possible extensions:

- Add additional cities
- Include wildfire indicators
- Test alternative risk score weighting methods
- Compare statistical and machine learning approaches
- Include additional environmental predictors

---

# Project Goal

This project demonstrates how statistical modeling and environmental data science can be used to understand relationships between extreme temperatures, PM2.5 concentrations, and environmental exposure risk across U.S. cities.
