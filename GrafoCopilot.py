import networkx as nx
import matplotlib.pyplot as plt


# Genera un ejemplo de grafos con 5 nodos y 6 aristas
# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(range(1, 6))

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# Print the graph
print(G)

# Genera la animacion del grafo anterior


# Create an empty graph
G = nx.Graph()
# Add nodes to the graph
G.add_nodes_from(range(1, 6))
# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# Generate the animation of the graph
pos = nx.spring_layout(G)  # Define the layout of the graph
fig, ax = plt.subplots()  # Create a figure and an axis
nx.draw(G, pos, with_labels=True, ax=ax)  # Draw the initial state of the graph

# Iterate over each edge and update the graph
for edge in G.edges():
    G.remove_edge(*edge)  # Remove the current edge
    nx.draw(G, pos, with_labels=True, ax=ax)  # Draw the updated graph
    plt.pause(1)  # Pause for 1 second to show the animation

plt.show()  # Show the final state of the graph