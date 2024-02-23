input_file = "temperature_data.csv"

# Data to be written to the CSV file
data = [
    ["Date", "Reading"],
    ["2024-01-01", "10°C"],
    ["2024-01-01", "70°F"],
    ["2024-01-01", "15°C"],
    ["2024-01-01", "62°F"],
    ["2024-01-01", "15°C"],
    ["2024-01-01", "17°C"],
    ["2024-01-01", "15°C"],
    ["2024-01-01", "61°F"]
]

# Write data to the CSV file
with open(input_file, 'w') as file:
    for row in data:
        file.write(','.join(row) + '\n')
