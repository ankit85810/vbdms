import db_helper
import re

def extract_sensor_number(command):
    """Extract sensor number from command using regex"""
    # Look for "sensor X" or "sensor number X" pattern
    sensor_match = re.search(r"sensor(?:\s+number)?\s+(\d+)", command.lower())
    if sensor_match:
        return int(sensor_match.group(1))
    
    # If not found, try to find any number in the command
    numbers = re.findall(r"\d+", command)
    if numbers:
        return int(numbers[0])
    
    return None

def process_command(command):
    """Process voice command and return appropriate response"""
    try:
        command = command.lower()
        
        # Extract sensor number
        sensor_num = extract_sensor_number(command)
        if not sensor_num:
            return "Sorry, I couldn't identify which sensor you're referring to."
        
        # Process commands based on keywords
        if "maximum" in command or "max" in command:
            data = db_helper.fetch_maximum_value(sensor_num)
            return f"Maximum value recorded for {data[0]['sensor_name']} is {data[0]['max_value']}."
            
        elif "minimum" in command or "min" in command:
            data = db_helper.fetch_minimum_value(sensor_num)
            return f"Minimum value recorded for {data[0]['sensor_name']} is {data[0]['min_value']}."
            
        elif "last value" in command or "latest" in command or "current" in command:
            data = db_helper.fetch_sensor_last_val(sensor_num)
            sensor_name = f"Sensor {sensor_num}"
            return f"Last value of {sensor_name} is {data[0][sensor_name]}."
            
        elif "status" in command:
            data = db_helper.fetch_sensor_status(sensor_num)
            return f"{data[0]['sensor_name']} is currently {data[0]['status']}"
            
        else:
            return "Sorry, I couldn't understand your command. Please try asking about maximum, minimum, last value, or status of a specific sensor."

    except ValueError:
        return "Sorry, could not understand the sensor number."
    except Exception as e:
        return f"An error occurred: {str(e)}"