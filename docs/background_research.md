# Scientific Background Research

## Environmental Health Data Observatory

## 1. Extreme Heat and Environmental Health

### What is an Extreme Temperature Event?

Extreme heat refers to temperatures that are unusually high compared with the normal climate conditions of a specific location. These events can occur as short periods of extreme temperatures or longer heat waves lasting several days.

Heat waves are commonly identified by comparing observed temperatures with historical averages for a region. Because daily temperature patterns vary significantly between climates, extreme heat is often defined relative to local conditions rather than using one universal temperature threshold.

For this project, daily maximum temperature will be used as the primary indicator of heat exposure.

### Temperature Variables

The project will use the following temperature variables:

| Variable | Purpose |
|----------|---------|
| temperature_max | Measures daily maximum temperature and identifies extreme heat conditions |
| temperature_mean | Represents average daily temperature exposure |

The primary variable will be:

**Daily Maximum Temperature (`temperature_max`)**

Reason:

- Captures the most intense heat experienced during a day.
- Helps identify extreme heat events.
- Allows comparison of heat exposure across different cities.

---

## Why Does Extreme Heat Matter for Health?

Extreme temperatures can increase environmental health risks by placing stress on the human body. During periods of high heat, the body must work harder to maintain normal temperature, increasing physiological stress.

Heat exposure has been associated with increased risks related to:

- Cardiovascular stress
- Respiratory difficulties
- Heat-related illness
- Increased vulnerability among older adults, children, and individuals with existing health conditions

Because cities have different climates and levels of heat exposure, analyzing temperature patterns across multiple locations can help identify differences in environmental risk.

---

# 2. PM2.5 and Air Quality

## What is PM2.5?

PM2.5 refers to fine particulate matter with a diameter of 2.5 micrometers or smaller. These particles are small enough to remain suspended in the atmosphere and can travel deep into the respiratory system.

PM2.5 concentration is commonly used as an indicator of air pollution because it represents exposure to small airborne particles that may negatively affect environmental and human health.

The dataset will measure:

where:

- μg = micrograms
- m³ = cubic meter of air

---

## Sources of PM2.5

PM2.5 can come from both natural and human sources.

Major sources include:

| Source | Example |
|--------|---------|
| Wildfires | Smoke particles released during fire events |
| Transportation | Vehicle emissions |
| Industrial activity | Manufacturing and power generation |
| Urban pollution | Dense traffic and human activity |

Different cities experience different PM2.5 patterns depending on climate, geography, population density, and pollution sources.

---

## Why Does PM2.5 Matter for Health?

Because of its small particle size, PM2.5 can penetrate deep into the respiratory system. Increased concentrations indicate higher levels of air pollution exposure.

Understanding PM2.5 patterns helps identify:

- Periods of poor air quality
- Differences between cities
- Potential environmental exposure risks

This project focuses on PM2.5 as an environmental exposure indicator rather than directly predicting individual health outcomes.

---

# 3. Relationship Between Extreme Heat and PM2.5

Temperature and air quality are often studied together because environmental conditions can influence both heat exposure and pollution levels.

Several mechanisms may connect extreme heat and PM2.5:

## Wildfire Smoke Events

Extreme heat and dry conditions can increase wildfire risk. Wildfires release large amounts of particulate matter, causing elevated PM2.5 concentrations.

Example:

- Western U.S. cities may experience periods of high temperature and increased PM2.5 due to wildfire smoke.

---

## Urban Heat Islands

Cities often experience higher temperatures than surrounding rural areas because buildings, roads, and other surfaces absorb and retain heat.

Urban areas may also have higher pollution levels due to:

- Traffic emissions
- Industrial activity
- Higher population density

This creates a potential overlap between heat exposure and air pollution exposure.

---

## Weather Conditions and Pollution Concentration

Weather affects how pollutants move through the atmosphere.

Variables such as:

- Wind speed
- Humidity
- Temperature

can influence whether pollutants disperse or remain concentrated.

For example:

- Strong winds may help disperse pollution.
- Stagnant conditions may allow pollutants to accumulate.

Because temperature alone may not explain PM2.5 changes, additional weather variables will be included in statistical analysis.

---

# 4. Statistical Methods

## Correlation Analysis

Correlation measures whether two variables change together.

This project will examine relationships such as:

\[
r = correlation(Temperature, PM2.5)
\]

The purpose is to answer:

> Do temperature and PM2.5 concentrations show a relationship across different cities?

Correlation values range from:

- +1: Strong positive relationship
- 0: No linear relationship
- -1: Strong negative relationship

Correlation does not prove that one variable causes another, but it helps identify patterns for further analysis.

---

## Regression Modeling

Regression analysis will be used to quantify relationships between environmental variables.

A possible model:

\[
PM2.5 = \beta_0 + \beta_1(Temperature) + \beta_2(Wind) + \beta_3(Humidity) + \epsilon
\]

Where:

- PM2.5 = predicted pollution concentration
- Temperature = heat exposure
- Wind = pollutant movement conditions
- Humidity = atmospheric conditions
- β values = estimated contribution of each variable
- ε = unexplained variation

The model helps answer:

> How much do environmental factors contribute to changes in PM2.5 concentrations?

---

# Environmental Risk Score

A risk score combines multiple environmental factors into one indicator.

A possible baseline model:

\[
Risk = 0.5(HeatScore)+0.5(PM2.5Score)
\]

Where:

- HeatScore represents relative temperature exposure.
- PM2.5Score represents relative pollution exposure.

The initial equal weighting approach provides a simple and transparent way to compare environmental conditions.

Future analysis may adjust weights using statistical relationships identified through regression models.

The risk score represents an environmental exposure indicator and does not directly predict individual health outcomes.

---

# Summary

This project investigates how temperature extremes and PM2.5 concentrations vary across U.S. cities and how statistical models can quantify relationships between environmental factors.

The analysis will combine:

- Environmental science concepts
- Weather and air quality data
- Correlation analysis
- Regression modeling
- Environmental risk indicators

to better understand patterns of environmental exposure.