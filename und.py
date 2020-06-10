import matplotlib.pyplot as plt 
import networkx as nx

grafo = nx.Graph()

print("Hi after inputs I gonna draw an undirected graph!\nPut the number of nodes, edges and the conections.")

n = int(input())
m = int(input())

nos = range(n)

arestas = []

for i in range(m):
    uv = input()
    u = int(uv[0])
    v = int(uv[2])

    arestas.append(tuple([u, v]))
    

grafo.add_nodes_from(nos)
grafo.add_edges_from(arestas)

nx.draw(grafo, with_labels=True)
plt.show()