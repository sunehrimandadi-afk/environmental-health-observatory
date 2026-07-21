import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect(
    "data/environmental_health.db"
)

print("Database connected!")

tables = pd.read_sql(
    """
    SELECT name 
    FROM sqlite_master
    WHERE type='table';
    """,
    conn
)

print(tables)

df = pd.read_sql(
    """
    SELECT *
    FROM environmental_daily;
    """,
    conn
)

print(df.head())
print(df.columns)
conn.close()