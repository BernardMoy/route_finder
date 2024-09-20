import pandas as pd
import sys
from collections import defaultdict

# Graph is defined here
G = defaultdict(list)

# Read from the excel data
df = pd.read_excel("stations_data.xlsx")

# Add the station codes to the dict
code_to_station = pd.Series(df.Station_name.values, index=df.Station_code).to_dict()
station_to_code = pd.Series(df.Station_code.values, index=df.Station_name).to_dict()
station_lower_to_code = pd.Series(df.Station_code.values, index=df.Station_name.str.lower()).to_dict()

# Add the line codes to the dict
code_to_line = pd.Series(df.Line_name.values, index=df.Line_code).to_dict()


# Keep track of the previous line and previous station
prev_line = None
prev_station = None
line = None

for index, row in df.iterrows():

    # Update line only when a new line is supplied
    if not pd.isna(row["Line"]):
        line = row["Line"]
        prev_station = None  # Reset prev station, as a new line is selected

    station = row["Station"]
    time = row["Time"]

    # Skip empty rows
    if pd.isna(station) or pd.isna(time):
        print(f"Skipping empty row number {index+2}")
        continue

    # Add an edge to the graph

    if prev_station:
        # only executes if there is a prev station, i.e. Not new line
        G[prev_station].append((station, float(time), str(line)))
        G[station].append((prev_station, float(time), str(line)))

    prev_station = station

print(G)

# Function to find the shortest 
def shortest(code_start : str, code_end : str) -> str:
    return ""

# Ask input for the start station
print("========================================")

code_start = input("Enter start station name / code:")

while code_start.upper() not in code_to_station and code_start.lower() not in station_lower_to_code:
    print("**Invalid start station provided!")
    code_start = input("Enter start station name / code:")

# Station code entered
if code_start.upper() in code_to_station:
    entered_code = code_start.upper()
    print(f"Start station: {code_to_station[entered_code]} ({entered_code})")

# Station name entered
else:
    code_start = station_lower_to_code[code_start.lower()]
    entered_name = code_to_station[code_start]
    print(f"Start station: {entered_name} ({code_start})")
    
# Ask input for end station
print("========================================")
code_end = input("Enter end station name / code:")

while code_end.upper() not in code_to_station and code_end.lower() not in station_lower_to_code:
    print("**Invalid end station provided!")
    code_end = input("Enter end station name / code:")

# Station code entered
if code_end.upper() in code_to_station:
    entered_code = code_end.upper()
    print(f"End station: {code_to_station[entered_code]} ({entered_code})")

# Station name entered
else:
    code_end = station_lower_to_code[code_end.lower()]
    entered_name = code_to_station[code_end]
    print(f"End station: {entered_name} ({code_end})")


# Start and end stations cannot be the same
if (code_start == code_end):
    print("**Start and end station cannot be the same!")
    sys.exit(1)

