import sqlite3
import pandas as pd


database = "data/environmental_health.db"


conn = sqlite3.connect(database)


cities = [
    "Phoenix",
    "LA",
    "Seattle",
    "Houston",
    "NY",
    "Sacramento"
]


all_data = []


for city in cities:

    file = f"data/processed/{city}_environment.csv"

    df = pd.read_csv(file)

    all_data.append(df)


combined = pd.concat(
    all_data,
    ignore_index=True
)


combined.to_sql(
    "environmental_daily",
    conn,
    if_exists="replace",
    index=False
)


print("Database created!")

print(combined.shape)


conn.close()
