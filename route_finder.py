import networkx as nx
import pandas as pd

G = nx.Graph()

stations = ['Station A', 'Station B', 'Station C', 'Station D']
G.add_nodes_from(stations)

# Add edges (connections between stations with distances and lines)
G.add_edge('Station A', 'Station B', weight=5, line='Red Line')
G.add_edge('Station B', 'Station C', weight=7, line='Blue Line')
G.add_edge('Station C', 'Station D', weight=3, line='Green Line')
G.add_edge('Station A', 'Station C', weight=9, line='Red Line')

# Visualize the graph with edge labels
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

import matplotlib.pyplot as plt
plt.show()
