import sys
from util import *

#ins = sys.stdin.readlines()
ins = ['dl\n', 'format=edgelist1\n', 'n=4\n', 'data:\n', '2 4 -61.500\n', '1 3 83.750\n', '1 2 -29.500\n', '3 4 78.000\n', '2 3 5.125']

#Inicializando as arestas e o número de vértices:
edges, n = getInsert(ins)

#Grafo:
graph = {'vertices': [v for v in range(1, (n+1) )],'edges': set(edges)}

kruskal(graph)