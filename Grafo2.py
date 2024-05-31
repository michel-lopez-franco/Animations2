import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear un grafo aleatorio
G = nx.random_geometric_graph(20, 0.2)

# Definir la ruta
ruta = [0, 5, 10, 15, 19]

# Configurar el dibujo del grafo
pos = nx.spring_layout(G)
fig, ax = plt.subplots(figsize=(8, 6))
nx.draw(G, pos, ax=ax, node_color='lightgray')

# Función para animar la ruta
def animate(i):
    if i < len(ruta):
        nodo_actual = ruta[i]
        nx.draw_networkx_nodes(G, pos, nodelist=[nodo_actual], node_color='r', ax=ax)
        if i > 0:
            nodo_anterior = ruta[i-1]
            nx.draw_networkx_edges(G, pos, edgelist=[(nodo_anterior, nodo_actual)], edge_color='r', width=2, ax=ax)
    return []

# Crear la animación
ani = FuncAnimation(fig, animate, frames=len(ruta)+1, interval=1000, repeat=False, blit=True)

# Mostrar la animación
plt.show()