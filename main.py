import csv
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from distance import meters_to_feet, feet_to_meters

def convert_temperatures_distance(input_file, output_file, target_unit, target_measure):
    """
    Read temperature data from the input file, convert temperatures to the target unit,
    and write the converted data to the output file.
    
    Parameters:
    - input_file: Input file path
    - output_file: Output file path
    - target_unit: Target temperature unit ('C' for Celsius, 'F' for Fahrenheit)
    """
    with open('temperature_distance_data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        
    converted_data = []
    for row in data:
        temperature = row[2]
        if '°C' in temperature:
            celsius = float(temperature.replace('°C', ''))
            if target_unit == 'F':
                converted_temperature = celsius_to_fahrenheit(celsius)
            else:
                converted_temperature = celsius
        elif '°F' in temperature:
            fahrenheit = float(temperature.replace('°F', ''))
            if target_unit == 'C':
                converted_temperature = fahrenheit_to_celsius(fahrenheit)
            else:
                converted_temperature = fahrenheit
        else:
            # Handle invalid temperature format
            converted_temperature = None
        distance = row[1]
        if 'm' in distance:
            meter = float(distance.replace('m', ''))
            if target_measure == 'ft':
                converted_distance = meters_to_feet(meter)
            else:
                converted_distance = meter
        elif 'ft' in distance:
            feet = float(distance.replace('ft', ''))
            if target_measure == 'm':
                converted_distance = feet_to_meters(feet)
            else:
                converted_distance = feet
        else:
            # Handle invalid temperature format
            converted_distance = None
            
        row[2] = f"{converted_temperature}{target_unit}"
        row[1] = f"{converted_distance}{target_measure}"
        converted_data.append(row)
        
    with open('converted_temperature_distance_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(converted_data)

# Example usage:
input_file = 'temperature_distance_data.csv'
output_file = 'converted_temperature_distance_data.csv'
target_unit = 'C' 
target_measure='ft' # Convert to Fahrenheit
convert_temperatures_distance(input_file, output_file, target_unit, target_measure)