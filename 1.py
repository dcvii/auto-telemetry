import psycopg2
from psycopg2 import sql

# Replace with your PostgreSQL credentials
conn = psycopg2.connect(
    host="localhost",
    database="your_database",
    user="your_username",
    password="your_password"
)

cur = conn.cursor()

tables = [
    """
    CREATE TABLE Vehicle_Data (
        Vehicle_ID VARCHAR(50) PRIMARY KEY,
        Timestamp TIMESTAMP NOT NULL
    )
    """,
    """
    CREATE TABLE Speed_Data (
        Vehicle_ID VARCHAR(50) REFERENCES Vehicle_Data(Vehicle_ID),
        Timestamp TIMESTAMP NOT NULL,
        Vehicle_Speed FLOAT NOT NULL,
        Acceleration FLOAT NOT NULL,
        Vehicle_Dynamics JSONB
    )
    """,
    """
    CREATE TABLE Engine_Data (
        Vehicle_ID VARCHAR(50) REFERENCES Vehicle_Data(Vehicle_ID),
        Timestamp TIMESTAMP NOT NULL,
        Engine_RPM FLOAT NOT NULL,
        Engine_Temperature FLOAT NOT NULL,
        Fuel_Consumption FLOAT NOT NULL
    )
    """,
    """
    CREATE TABLE Location_Data (
        Vehicle_ID VARCHAR(50) REFERENCES Vehicle_Data(Vehicle_ID),
        Timestamp TIMESTAMP NOT NULL,
        GPS_Location POINT NOT NULL,
        Odometer_Reading FLOAT NOT NULL
    )
    """,
    """
    CREATE TABLE Tire_Battery_Data (
        Vehicle_ID VARCHAR(50) REFERENCES Vehicle_Data(Vehicle_ID),
        Timestamp TIMESTAMP NOT NULL,
        Tire_Pressure JSONB NOT NULL,
        Battery_Voltage FLOAT NOT NULL
    )
    """,
    """
    CREATE TABLE Brake_Diagnostics_Data (
        Vehicle_ID VARCHAR(50) REFERENCES Vehicle_Data(Vehicle_ID),
        Timestamp TIMESTAMP NOT NULL,
        Brake_Status BOOLEAN NOT NULL,
        DTCs JSONB
    )
    """,
    """
    CREATE TABLE Crash_Data (
        Vehicle_ID VARCHAR(50) REFERENCES Vehicle_Data(Vehicle_ID),
        Timestamp TIMESTAMP NOT NULL,
        Crash_Impact_Data JSONB
    )
    """
]

for table_query in tables:
    cur.execute(table_query)

# commit the changes
conn.commit()

# close communication with the database
cur.close()
conn.close()
