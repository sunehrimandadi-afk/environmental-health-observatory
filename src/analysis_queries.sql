SELECT 
    city,
    date,
    pm25
FROM environmental_daily
ORDER BY pm25 DESC
LIMIT 20;

SELECT
    city,
    AVG(mean_temperature) AS avg_temperature
FROM environmental_daily
GROUP BY city;

SELECT
    city,
    AVG(mean_temperature) AS avg_temp,
    AVG(pm25) AS avg_pm25
FROM environmental_daily
GROUP BY city
ORDER BY avg_pm25 DESC;