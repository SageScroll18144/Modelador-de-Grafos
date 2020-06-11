import matplotlib.pyplot as plt 
import networkx as nx

def main(n, m):
    grafo = nx.DiGraph()

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

if __name__ == '__main__':
    while True:
        print("*Hi after inputs I gonna draw an directed graph!*\nIf you want to exit, type 'q', else type the number of nodes and edges.\n>", end=" ")
        a = input()
        print("> ", end="")
        if a == 'q':
            break

        n = int(a)
        m = int(input())
        
        print("Conections.:")

        main(n, m)