import sys
from collections import defaultdict

ins = sys.stdin.readlines()
#ins = ['dl\n', 'format=edgelist1\n', 'n=5\n', 'data:\n', '1 3 78.250\n', '2 3 76.750\n', '3 5 63.500\n', '3 2 51.250\n', '3 1 62.875\n', '4 3 13.625\n', '4 2 1.625\n', '4 1 14.125\n', '5 2 10.875\n', '5 1 40.000']


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

#

def dijsktra(graph, initial_vertex):
    #Inicializando os arrays de visitados e caminhos a partir do vertice inicial:
    visited = {initial_vertex: 0}
    path = {}

    #Pegando o conjunto de nós do grafo em uma variável, pois retiraremos nós à cada
    # interação do algoritmo:
    nodes = set(graph.nodes)


    #Enquanto houver nós, faça:
    while nodes: 

        min_node = None
        #Fazendo a escolha do nó com menor estimativa dentre os nós abertos:
        for node in nodes:
            
            if node in visited:
                if min_node is None:
                    min_node = node
                
                elif visited[node] < visited[min_node]:
                    min_node = node

        #

        #Se não temos mais nós abertos, paramos a interação:
        if min_node is None:
            break

        #"Fechando" o nó:
        nodes.remove(min_node)
        
        #Pegando o "peso" dele:
        current_weight = visited[min_node]

        #Para cada vértice nas adjacências desse nó, faremos o "relaxamento":
        for edge in graph.edges[min_node]:
            
            weight = current_weight + graph.distances[(min_node, edge)]
            
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

#

def getInsert(ins):
    edges = []

    #Pegando n:
    n = ins[2].split("=")[1]
    #n= str(ins[2][2]) + str(ins[2][3]).strip()

    #print("N:{}".format(n))

    #Aproveitando os espaços p/ usar o split e pegar os números das arestas:
    for element in ins:
        #print("Element:  {}".format(element),"Element split: {}".format(element.split()) )
        #for s in element.split():
        #    print (s, s.isdigit(), is_float(s))

        #Pegando cada número do elemento de entrada:    
        #number = ["%.3f" % float(s) for s in element.split() if is_float(s)]
        element = element.split()
               
        #Pegando somente os splits que têm números:
        if len(element) > 1:
            edge = (float(element[2]), int(element[0]), int(element[1]) )
            edges.append(edge)

        #else:
        #    if(element[0][0] == 'n'):
        #        test = element[0].split("=")
        #        print(test[1])       

    #print("Edges: {}".format(edges))

    return edges, int(n)

#

#Inicializando as arestas e o número de vértices:
edges, n = getInsert(ins)
#print(edges)

#Criando os vértices:
vertices = [v for v in range(1, (n+1))]
#Grafo:
#graph = {
#        'vertices': [v for v in range(1, (n+1) )],
#        'edges': set(edges)
#        }

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
    
 
