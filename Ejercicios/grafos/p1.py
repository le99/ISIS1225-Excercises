import config
from DISClib.ADT import graph as g
from DISClib.DataStructures import listiterator

# Cargar los siguientes datos a un grafo no dirigido:

datos = [
    {'id': 1, 'adj':[2, 3]},
    {'id': 2, 'adj':[1, 3]},
    {'id': 3, 'adj':[2, 3]},
    {'id': 4, 'adj':[]}
]

# Imprimir los vertices adjacentes al segundo vertice


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


# g.insertVertex(grafo, "1")
# g.insertVertex(grafo, "2")
# g.addEdge(grafo, "1", "2")


