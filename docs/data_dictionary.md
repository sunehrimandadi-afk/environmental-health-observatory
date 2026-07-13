# Data Dictionary

## Dataset Description

This dataset contains daily weather and air quality measurements from selected U.S. cities to analyze the relationship between extreme heat and PM2.5 pollution and develop an environmental risk indicator using statistical modeling.

---

## Variables

| Variable | Type | Units | Description |
|---|---|---|---|
| date | Date | YYYY-MM-DD | Date of observation |
| city | Category | N/A | U.S. city location |
| latitude | Numeric | Degrees | Latitude coordinate of city |
| longitude | Numeric | Degrees | Longitude coordinate of city |
| temperature_max | Numeric | °F | Maximum daily temperature representing heat exposure |
| temperature_mean | Numeric | °F | Average daily temperature |
| humidity | Numeric | % | Relative humidity |
| wind_speed | Numeric | km/h | Wind speed |
| precipitation | Numeric | mm | Total daily precipitation |
| PM2.5 | Numeric | μg/m³ | Fine particulate matter concentration representing air pollution exposure |
| heat_score | Numeric | Z-score | Standardized heat exposure score based on maximum daily temperature |
| pollution_score | Numeric | Z-score | Standardized PM2.5 exposure score |
| risk_score | Numeric | Z-score | Combined environmental risk indicator based on heat and pollution exposure |

---

## Data Sources

Weather Data:
- Open-Meteo API
