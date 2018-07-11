import sys
from util import getInsert, Graph, dijsktra

#ins = sys.stdin.readlines()
ins = ['dl\n', 'format=edgelist1\n', 'n=5\n', 'data:\n', '1 3 78.250\n', '2 3 76.750\n', '3 5 63.500\n', '3 2 51.250\n', '3 1 62.875\n', '4 3 13.625\n', '4 2 1.625\n', '4 1 14.125\n', '5 2 10.875\n', '5 1 40.000']


#Inicializando as arestas e o número de vértices:
edges, n = getInsert(ins)

#Criando os vértices:
vertices = [v for v in range(1, (n+1))]

graph = Graph()

#Populando os nós do Grafo:
for v in vertices:
    graph.add_node(v)

#Populando as arestas do Grafo:
for e in edges:
    graph.add_edge(e[1], e[2], e[0])

#Executando Dijkstra:
visited, path = dijsktra(graph, 1)

#Imprimindo o resultado:
for vertex in graph.nodes:
    try:
        print(vertex, "%.3f" % float(visited[vertex]))
    except Exception:
        print(vertex, "INFINITO")
    
 
