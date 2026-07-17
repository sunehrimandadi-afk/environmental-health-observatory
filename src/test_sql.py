import sqlite3
import pandas as pd


conn = sqlite3.connect(
    "data/environmental_health.db"
)


query = """
SELECT city, AVG(pm25)
FROM environmental_daily
GROUP BY city;
"""


result = pd.read_sql(query, conn)

print(result)


conn.close()
