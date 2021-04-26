import config
from DISClib.ADT import graph as g
from DISClib.DataStructures import listiterator

def comparefunction(searchname, element):
    if (searchname == element['key']):
        return 0
    elif (searchname < element['key']):
        return -1
    return 1

grafo = g.newGraph(datastructure='ADJ_LIST',
                        directed=False,
                        size=14000,
                        comparefunction=comparefunction)

# Hacer un metodo que imprima un grafo no dirigido de esta forma:
# Vertice 1: Vertice-adyacente 1, Vertice-adyacente 2 
# Vertice 2: Vertice-adyacente 1, Vertice-adyacente 2 
# Vertice 3: Vertice-adyacente 1, Vertice-adyacente 2 

g.insertVertex(grafo, "1")
g.insertVertex(grafo, "2")
g.insertVertex(grafo, "3")
g.addEdge(grafo, "1", "2")

def toString(grafo):
    pass