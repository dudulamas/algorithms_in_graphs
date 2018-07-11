INFINITY, WHITE, GRAY, BLACK = -1, 0, 1, 2

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
    '''
    Função para capturar os dados de entrada da ferramenta de geração de grafos do Gephi.

    A entrada deve ser parecida com o seguinte array de strings: 
    ins = ['dl\n', 'format=edgelist1\n', 'n=10\n', 'data:\n', '2 9\n', '3 8\n', '5 7\n', '6 9\n', '8 10']
    '''
    
    edges = []

    #Pegando o número de vértices do grafo:
    n = ins[2].split("=")[1]

    #Aproveitando os espaços p/ usar o split e pegar os números das arestas:
    for element in ins:
       
        #Pegando cada número do elemento de entrada:    
        element = element.split()

        #print(element)
               
        #Pegando somente os splits que têm números:
        if len(element) > 1:
            
            #Se as arestas não possuírem peso, não haverá o terceiro elemento que é o peso:
            if len(element) == 2:
                edge = (int(element[0]), int(element[1]) )
                edges.append(edge)
            
            #Se possuir peso:
            else:
                edge = (float(element[2]), int(element[0]), int(element[1]) )
                edges.append(edge)
       

    #print(edges, n)

    return edges, int(n)

#

def dfs(vertex, edges, u=None):
    '''
    Implementação de uma busca em profundidade no grafo.

    vertex: conjunto de vértices do grafo;
    edges: conjunto de arestas;
    u: vértice inicial
    '''
    
    #Notar que sempre que formos atualizar algo nos vetores color, distance e father,
    # diminuiremos 1, pois o vetor de vertices se inicia em 1.
    
    colors = [WHITE] *          len(vertex)
    distances = [INFINITY] *    len(vertex)
    fathers = [None] *          len(vertex)
    ends = [INFINITY] *         len(vertex)

    if u:
        _operation_dfs(edges, u, 0, colors, distances, fathers, ends)

    else:
        for v in vertex:
            if color[v] == WHITE:
                _operation_dfs(edges, u, time, colors, distances, fathers, ends)

#

def bfs(vertex, edges, v):
    '''
    Função para fazer busca em largura em um grafo.

    vertex: lista de vértices do grafo;
    edges: lista de arestas do grafo;
    v: vértice inicial;

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
        u_adjacency = _adjacency(edges, u)
        
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

def _operation_dfs(edges, u, time, colors, distances, fathers, ends):
    '''
    Algoritmo que criará a árvore dfs com raiz em u.
    
    '''

    colors[u] = GRAY
    time = time + 1
    distances[u] = time

    for v in _adjacency(edges,u):
        if colors[v] == WHITE:
            fathers[v] = u
            operation_dfs(edges, v, time, colors, distances, fathers, ends)

    colors[u] = BLACK
    time = time + 1
    ends[u] = time 

#

def _adjacency(edges, vertex):
    '''
    Função para retornar a adjacência de um vértice;

    '''
    adjacency = []
    for edge in edges:
        if vertex == edge[0]:
            adjacency.append(edge[1])
        elif vertex == edge[1]:
            adjacency.append(edge[0])

    return adjacency

#


'''
Funções utilizadas na implementação do segundo trabalho. 

Foi solicitado a construção de uma AGM.
'''
parent = dict()
rank = dict()

def kruskal(graph):
    for vertice in graph['vertices']:
        _make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if _find(vertice1) != _find(vertice2):
            _union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    
    _sum(minimum_spanning_tree)

    return minimum_spanning_tree

#

def _make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0
#

def _find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = _find(parent[vertice])
    return parent[vertice]

#

def _union(vertice1, vertice2):
    root1 = _find(vertice1)
    root2 = _find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

#

def _sum(minimum_spanning_tree):
    count = 0
    for edge in minimum_spanning_tree:
        count+=edge[0]

    print("%.3f" % float(count))

#

'''
Funções utilizadas na implementação do terceiro trabalho. 

Foi solicitado a construção de caminhos mínimos.
'''

class Graph:
    def __init__(self):
        from collections import defaultdict

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

