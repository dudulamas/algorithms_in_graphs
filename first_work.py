import sys
ins = sys.stdin.readlines()
#ins = ['dl\n', 'format=edgelist1\n', 'n=10\n', 'data:\n', '2 9\n', '3 8\n', '5 7\n', '6 9\n', '8 10']

#edges = set([(2,9), (3,8), (5, 7), (6, 9), (8, 10)])

INFINITY, WHITE, GRAY, BLACK = -1, 0, 1, 2
#print(graph)

class Queue(object):
    def __init__(self):
        self._elements = []

    def remove(self):
        try:
            return self._elements.pop(0)
        except:
            return None

    def add(self, value):
        self._elements.insert(len(self._elements), value)

    def empty(self):
        return False if self._elements else True

    def __str__(self):
        return str(self._elements)
#

def getInsert(ins):
    edges = []

    #Pegando n:
    n=str(ins[2][2]) + str(ins[2][3]).strip()

    #Aproveitando os espaços p/ usar o split e pegar os números das arestas:
    for element in ins:
        number = [int(s) for s in element.split() if s.isdigit()]
        
        if number:
            edges.append(tuple(number))

    #print(n,"\n", edges)
    return edges, int(n)

#

def dfs(vertex, edges, u=None):
    #Notar que sempre que formos atualizar algo nos vetores color, distance e father,
    # diminuiremos 1, pois o vetor de vertices se inicia em 1.
    colors = [WHITE] *          len(vertex)
    distances = [INFINITY] *    len(vertex)
    fathers = [None] *          len(vertex)
    ends = [INFINITY] *         len(vertex)

    if u:
        operation_dfs(edges, u, time=0, colors, distances, fathers, ends)

    else:
        for v in vertex:
            if color[v] == WHITE:
                operation_dfs(edges, u, time, colors, distances, fathers, ends)

#

def operation_dfs(edges, u, time, colors, distances, fathers, ends):
    '''
    Algoritmo que criará a árvore dfs com raiz em u.
    '''
    colors[u] = GRAY
    time = time + 1
    distances[u] = time

    for v in adjacency(edges,u):
        if colors[v] == WHITE:
            fathers[v] = u
            operation_dfs(edges, v, time, colors, distances, fathers, ends)

    colors[u] = BLACK
    time = time + 1
    ends[u] = time 

#

def bfs(vertex, edges, v):
    '''
    Função para fazer busca em largura em um grafo.

    return: lista de adjacências de um vértice no grafo.
    '''
    #Notar que sempre que formos atualizar algo nos vetores color, distance e father,
    # diminuiremos 1, pois o vetor de vertices se inicia em 1.
    colors = [WHITE] * len(vertex)
    distances = [INFINITY] * len(vertex)
    fathers = [None] * len(vertex)

    #print("Start BFS: ", colors, distances, fathers)
    
    #Inicialização. Pintando todos os vértices do conjunto de Vérties - {s} de branco, 
    # colocando a distância p/ infinito:
    vertex_minusV = list(vertex)
    vertex_minusV.remove(v)
    #for element in vertex_minusV:
    #    color[element] = WHITE
    #    distance[element] = INFINITY
    #    pi[element] = None
    
    #Informando que o vértice de análise v já foi visitado e o inicializando:
    colors[v-1] = GRAY
    distances[v-1] = 0
    fathers[v-1] = None

    #Criando a fila:
    queue = Queue()

    #Enfilando o elemento v:
    queue.add(v)

    while not queue.empty():
        #Retirando o primeiro elemento da fila:
        u = queue.remove()
        #Pegando os seus vértices adjacentes:
        u_adjacency = adjacency(edges, u)
        
        #P/ cada vertice na adjacencia de u, fazer:
        for element in u_adjacency:
            if colors[element-1] == WHITE:
                colors[element-1] = GRAY
                distances[element-1] = distances[u-1] + 1
                fathers[element-1] = u
                queue.add(element)
        
        colors[u-1] = BLACK

        #Organizando o valor das distâncias, pois inicializamos todas em 0:
        #for element in distances:

    #print("Result BFS: ", colors, distances, fathers)
    
    adjacencyList = set()
    index = 0
    while index < len(distances):
        #Se a distância for diferente de infinito e de zero, então conseguimos chegar
        # no vértice: 
        if distances[index] != INFINITY and distances[index] != 0:
            adjacencyList.add(vertex[index])

        index=index+1

    return adjacencyList
#

def adjacency(edges, vertex):
    adjacency = []
    for edge in edges:
        if vertex == edge[0]:
            adjacency.append(edge[1])
        elif vertex == edge[1]:
            adjacency.append(edge[0])

    return adjacency

#

def exercise(element, adjacencyList, arrayOfPrinted):
    
    #Se o elemento ainda não foi printado:
    if not arrayOfPrinted[element-1]:
        #Array que será impresso:
        elements = "" + str(element)
        arrayOfPrinted[element-1] = True

        if adjacencyList:
            #Fazendo a ordenação:
            sortedList = sorted(adjacencyList)
            #Para cada elemento da lista de adjacência, o imprimir e marcar que ele foi
            # impresso:
            for element in sortedList:
                elements = elements + " " + str(element)
                #print(" ", element)
                printed[element-1] = True

        
        print(elements)

#

#Inicializando as arestas e o número de vértices:
edges, n = getInsert(ins)

#Graph: (vertex = 1 a 10):
graph = {'vertex': [v for v in range(1,(n+1))], 'edges': edges}
 

#Vetor armazenando os grafos já impressos:
printed = [False] * len(graph['vertex'])
#print("Set of vertex: ", graph['vertex'],"\nSet of edges: ", graph['edges'])

for element in graph['vertex']:
    adjacencyList = bfs(vertex=graph['vertex'], edges=graph['edges'], v=graph['vertex'][element-1])
    exercise(element, adjacencyList, printed)

























#edges, n = get_insert(ins)

#adjacencyList = build_adjacencyList(edges=edges, numberVertex=n)

#build_relatedComponents(adjacencyList)

#print(adjacencyList)
#print(vertex,'\n', edges) 

