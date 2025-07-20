import osmnx as ox

# A structured dictionary is more reliable for geocoding
place_query = {
    'suburb': 'Powai',
    'city': 'Mumbai',
    'state': 'Maharashtra',
    'country': 'India'
}

print(f"Downloading road network for Powai, Mumbai...")

# Download the road network graph using the new query
G = ox.graph_from_place(place_query, network_type='drive')

print("Download complete!")
print(f"Graph has {len(G.nodes)} nodes (intersections).")
print(f"Graph has {len(G.edges)} edges (roads).")

# Save the graph to a file
ox.save_graphml(G, "powai_map.graphml")
print("Graph saved to powai_map.graphml")