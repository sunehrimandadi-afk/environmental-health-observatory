# Data Sources

## Open-Meteo Weather API

### Purpose

The Open-Meteo API provides historical weather data that will be used to analyze temperature patterns and PM2.5  across selected U.S. cities with different climates. 

## Variables Collected

| Variable | API Name | Purpose |
|---|---|---|
| Date | time | Tracks changes over time |
| Maximum Temperature | temperature_2m_max | Identifies extreme heat days |
| Minimum Temperature | temperature_2m_min | Measures daily temperature variation |
| Mean Temperature | temperature_2m_mean | Compares average conditions |
| Relative Humidity | relative_humidity_2m_mean | Examines heat stress conditions |
| Wind Speed | wind_speed_10m_mean | Studies effects on air pollution dispersion |

## API Information

- Historical data available: Yes
- Location format: Latitude and longitude coordinates
- Temperature units: Celsius (can be converted to Fahrenheit)
- Time format: Observations each day from May 1, 2022 - September 30, 2025, which includes 3 summers

## Planned Locations

Cities will be selected based on differences in climate and pollution patterns. Coordinates are used to query weather and air-quality APIs. 

| City | State | Latitude | Longitude | Climate / Pollution Rationale |
|---|---|---:|---:|---|
| Phoenix | AZ | 33.4484 | -112.0740 | Very hot desert climate; frequent extreme heat events and high heat exposure |
| Sacramento | CA | 38.5816 | -121.4944 | Hot inland climate; wildfire smoke exposure and seasonal PM2.5 increases |
| Los Angeles | CA | 34.0522 | -118.2437 | Urban heat island effects; traffic-related air pollution and ozone exposure |
| Seattle | WA | 47.6062 | -122.3321 | Cooler Pacific Northwest climate; comparison city with fewer extreme heat events |
| Houston | TX | 29.7604 | -95.3698 | Hot and humid climate; industrial emissions and high heat stress risk |s