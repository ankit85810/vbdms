import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host="35.193.157.62",
        user = "root",
        password="Ankprit@85810",
        database = "SensorDB"
    )
    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit :
        connection.commit()
    cursor.close()
    connection.close()


def fetch_maximum_value(x):
    with get_db_cursor() as cursor:
        sensor_column = f"Sensor {x}"
        query = f"SELECT '{sensor_column}' AS sensor_name, MAX(`{sensor_column}`) AS max_value FROM sensordata;" 
        cursor.execute(query)
        data = cursor.fetchall()
        return data
    
def fetch_minimum_value(x):
    with get_db_cursor() as cursor:
        sensor_column = f"Sensor {x}" 
        query = f"SELECT '{sensor_column}' AS sensor_name, MIN(`{sensor_column}`) AS min_value FROM sensordata;"       
        cursor.execute(query)  
        data = cursor.fetchall() 
        return data

    
def fetch_sensor_status(x):
    with get_db_cursor() as cursor:
        cursor.execute(f"SELECT sensor_name, status FROM sensorstatus WHERE sensor_name = 'Sensor {x}';")
        data = cursor.fetchall()
        return data
    
def fetch_sensor_last_val(x):
    with get_db_cursor() as cursor:
        sensor_column = f"Sensor {x}"  
        query = f"SELECT `{sensor_column}` FROM sensordata ORDER BY time_stamp DESC LIMIT 1"
        
        cursor.execute(query)  
        result = cursor.fetchall()

        return result


    

if __name__ == "__main__":
    x = 12
    # data = fetch_maximum_value(x)
    # print(data)
    # data = fetch_minimum_value(x)
    # print(data) 
    # data = fetch_sensor_status(x)
    # print(data)
    # data = fetch_sensor_last_val(x)
    # print(data)
