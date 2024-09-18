import networkx as nx
import pandas as pd

G = nx.MultiGraph()

# Read from the excel data
df = pd.read_excel("stations_data.xlsx")

# Extract all stations data to be used to create graph
stations_data = df["Station"].dropna().replace("", None).unique()
stations_list = list(stations_data)

# Add the stations node to the graph
G.add_nodes_from(stations_list)



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
        print(f"Skipping empty row number {index}")
        continue

    # Add an edge to the graph
    if not prev_line:
        prev_line = line

    if prev_station:
        G.add_edge(prev_station, station, weight = float(time), line = str(line))

    prev_station = station

print("Graph edges with attributes:", G.edges(data=True))




# Draw the graph
import matplotlib.pyplot as plt

# Set positions for nodes
pos = nx.spring_layout(G)

# Draw the graph
plt.figure(figsize=(12, 8))

# pip install https://github.com/paulbrodersen/netgraph/archive/dev.zip
from netgraph import MultiGraph 

labels = {(u, v, k): f'{G[u][v][k]["weight"]}' for u, v, k in G.edges(keys=True)}
MultiGraph(G, node_labels=True, edge_labels=labels, edge_color='tab:blue')

plt.show()