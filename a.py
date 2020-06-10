import matplotlib.pyplot as plt 
import networkx as nx

grafo = nx.DiGraph()

nos = range(1,4)

arestas = [(1,2), (2,3), (3,4), (4,2)]

grafo.add_nodes_from(nos)
grafo.add_edges_from(arestas)

nx.draw(grafo, with_labels=True)
plt.show()