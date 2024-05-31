import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Crear un grafo dirigido
G = nx.DiGraph()
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'),
    ('B', 'E'), ('D', 'E'), ('E', 'F'), ('F', 'G')
]
G.add_edges_from(edges)

# Inicializar la figura
fig, ax = plt.subplots(figsize=(8, 8))
pos = nx.spring_layout(G)  # Posiciones de los nodos

# Dibuja el grafo completo en gris
nx.draw_networkx_nodes(G, pos, node_color='grey', node_size=700)
nx.draw_networkx_edges(G, pos, edge_color='grey')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

# Lista para guardar los estados de la animación
visited_nodes = []
visited_edges = []

# Función de animación para mostrar la exploración BFS
def bfs_animation():
    queue = ['A']  # Cola de BFS iniciada con el nodo 'A'
    while queue:
        node = queue.pop(0)
        if node not in visited_nodes:
            visited_nodes.append(node)
            for neighbor in G.neighbors(node):
                if neighbor not in visited_nodes:
                    visited_edges.append((node, neighbor))
                    queue.append(neighbor)
                yield

# Animar BFS
bfs_gen = bfs_animation()  # Generador de BFS

def update(num):
    ax.clear()
    nx.draw_networkx_nodes(G, pos, node_color='grey', node_size=700)
    nx.draw_networkx_edges(G, pos, edge_color='grey')
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, edgelist=visited_edges, edge_color='blue', width=2)

ani = animation.FuncAnimation(fig, update, frames=bfs_gen, repeat=False)

plt.show()
