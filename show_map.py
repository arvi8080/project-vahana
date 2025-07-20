import osmnx as ox
import matplotlib.pyplot as plt

# Load the graph from the file you saved
G = ox.load_graphml("powai_map.graphml")

print("Plotting graph...")

# Plot the graph and display it
fig, ax = ox.plot_graph(G, show=False, close=False)
plt.show()

print("Plot closed.")