# Implementing the whole code and logic from the 'aus_idk.ipynb' notebook into a python script
# Loading the needed modules
import geopandas as gpd
import networkx as nx
import matplotlib.pyplot as plt
import os

# Loading the data
aus_df = gpd.read_file("../data/aus_clean.json")
# Finding the neighbours for each region
neighbours = {}
for i, row in aus_df.iterrows():
    neighbours[i] = [] # initialize the neighbour index values
    for j, other_row in aus_df.iterrows():
        if i!=j and row['geometry'].intersects(other_row.geometry):
            neighbours[i].append(j)

# Creating a 'helper' graph for coloring
G = nx.Graph()
# Adding nodes similar to the original map
for i in range(len(aus_df)):
    G.add_node(i)
#Adding edges based on the neighbours adjacency list
for i, nbrs in neighbours.items():
    for nbr in nbrs:
        G.add_edge(i, nbr)

# Coloring the graph using a greedy algorithm, DSATUR strategy
colors = nx.coloring.greedy_color(G, strategy='DSATUR')
# Mapping the colors back to the GeoDataframe based on the indexes
aus_df['color'] = aus_df.index.map(colors)
# Mapping with the question's Red, Blue, Green colour scheme
color_map = {
    0: "#C41616",  # red
    1: "#2196F3",  # blue
    2: "#5EFF00",  # green
}

aus_df["color"] = aus_df["color"].map(color_map)

# Final plotting of the map with the new colour scheme
fig, ax = plt.subplots(figsize=(10,10))
aus_df.plot(
    ax=ax,
    color=aus_df["color"],
    edgecolor='black'
)
plt.title("Map of Australia's 5 main regions: Now with colouring!")
plt.axis('off')
plt.savefig('../output/aus_coloured.png')
plt.show()