import time
import random
import mysql.connector
from datetime import datetime

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="password",  
    database="SensorDB"
)
cursor = db.cursor()

while True:
    
    cursor.execute("SELECT sensor_name FROM sensorstatus")
    all_sensors = [row[0] for row in cursor.fetchall()]

    
    if all_sensors:
        
        for sensor in all_sensors:
            new_status = random.choice(["Active", "Inactive"])
            cursor.execute("UPDATE sensorstatus SET status = %s WHERE sensor_name = %s", (new_status, sensor))
        db.commit()
    
    cursor.execute("SELECT sensor_name FROM sensorstatus WHERE status = 'Active'")
    active_sensors = [row[0] for row in cursor.fetchall()]

    if not active_sensors:
        print("No active sensors. Skipping this cycle.")
        time.sleep(1)
        continue

    sensor_values = {sensor: round(random.uniform(10, 100), 2) for sensor in active_sensors}

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    
    columns = "`time_stamp`, " + ", ".join([f"`{sensor}`" for sensor in sensor_values.keys()])
    values = f"'{current_time}', " + ", ".join([str(v) for v in sensor_values.values()])
    query = f"INSERT INTO sensordata ({columns}) VALUES ({values})"

    try:
        cursor.execute(query)
        db.commit()
        print(f"Inserted at {current_time}: {sensor_values}")
    except Exception as e:
        print("Error:", e)
        db.rollback()

    time.sleep(500)  # Wait 500 seconds before next update
