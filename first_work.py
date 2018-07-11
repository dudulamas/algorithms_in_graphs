import sys
from util import *

#ins = sys.stdin.readlines()
ins = ['dl\n', 'format=edgelist1\n', 'n=10\n', 'data:\n', '2 9\n', '3 8\n', '5 7\n', '6 9\n', '8 10']


def exercise(element, adjacencyList, arrayOfPrinted):
    '''
    Função para imprimir o solicitado abaixo:

    Escreva um programa que determine as componentes conexas do grafo não-direcionado recebido como entrada.
    '''
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

#O Grafo terá uma lista de vértices de 1 ao resultado de 'n':
graph = {'vertex': [v for v in range(1,(n+1))], 'edges': edges}

#Vetor armazenando os grafos já impressos:
printed = [False] * len(graph['vertex'])

for element in graph['vertex']:
    adjacencyList = bfs(vertex=graph['vertex'], edges=graph['edges'], v=graph['vertex'][element-1])
    exercise(element, adjacencyList, printed)

























#edges, n = get_insert(ins)

#adjacencyList = build_adjacencyList(edges=edges, numberVertex=n)

#build_relatedComponents(adjacencyList)

#print(adjacencyList)
#print(vertex,'\n', edges) 

