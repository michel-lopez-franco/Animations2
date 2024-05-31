import networkx as nx
import networkx as nx
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt



# Genera un ejemplo de grafos con 10 nodos y 6 aristas
G = nx.gnm_random_graph(10, 6)
pos = nx.spring_layout(G)

# Función para actualizar el grafo en cada frame de la animación

def update(frame):
    plt.clf()
    nx.draw(G, pos, with_labels=True)
    plt.title(f"Frame {frame+1}")

# Crea la animación
animation = FuncAnimation(plt.gcf(), update, frames=10, interval=1000, repeat=True)

# Muestra la animación
plt.show()