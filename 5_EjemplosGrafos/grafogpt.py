import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Crear un grafo
G = nx.grid_2d_graph(4, 4)  # crea una red de 4x4

# Definir la ruta que se va a animar
path = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]

# Inicializa la figura de matplotlib
fig, ax = plt.subplots(figsize=(6, 6))
pos = {(x, y): (y, -x) for x, y in G.nodes()}
nx.draw(G, pos, ax=ax, node_color='lightgrey', with_labels=True, node_size=600)

# Función de animación para mostrar la ruta
def update(num):
    ax.clear()
    # Dibuja el grafo
    nx.draw(G, pos, ax=ax, node_color='lightgrey', with_labels=True, node_size=600)
    # Dibuja la ruta hasta el punto actual de la animación
    nx.draw_networkx_nodes(G, pos, nodelist=path[:num+1], node_color='blue', node_size=600)
    if num > 0:
        edges = [(path[i], path[i+1]) for i in range(num)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=2, edge_color='blue')

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=len(path), interval=100, repeat=True)

plt.show()
