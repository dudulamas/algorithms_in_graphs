import sys
ins = sys.stdin.readlines()

parent = dict()
rank = dict()

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

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
#

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0
#

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

#

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

#

def sum(minimum_spanning_tree):
    count = 0
    for edge in minimum_spanning_tree:
        count+=edge[0]

    print("%.3f" % float(count))

#

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    
    sum(minimum_spanning_tree)

    return minimum_spanning_tree

#

#Inicializando as arestas e o número de vértices:
edges, n = getInsert(ins)

#Grafo:
graph = {
        'vertices': [v for v in range(1, (n+1) )],
        'edges': set(edges)
        }

kruskal(graph)