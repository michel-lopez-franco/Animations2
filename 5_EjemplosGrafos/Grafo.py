import networkx as nx
import matplotlib.pyplot as plt


#G = nx.petersen_graph()
G = nx.Graph()
G.add_node(1)

G.add_nodes_from([2, 3])
#G.add_nodes_from([(4, {"color": "red"}), (5, {"color": "green"})])


G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*

#G.add_edges_from([(1, 2, {'color': 'red'})])
G.add_edges_from([(1, 2), ], color='red')

subax1 = plt.subplot(121)

nx.draw(G, with_labels=True, font_weight='bold')



plt.show()

