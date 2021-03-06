import config
from DISClib.ADT import graph as gr
from DISClib.ADT import list as lt

def comparefunction(searchname, element):
    if (searchname == element['key']):
        return 0
    elif (searchname < element['key']):
        return -1
    return 1

grafo = gr.newGraph(datastructure='ADJ_LIST',
                        directed=False,
                        size=14000,
                        comparefunction=comparefunction)

# Hacer un metodo que imprima un grafo no dirigido de esta forma:
# Vertice 1: Vertice-adyacente 1, Vertice-adyacente 2 
# Vertice 2: Vertice-adyacente 1, Vertice-adyacente 2 
# Vertice 3: Vertice-adyacente 1, Vertice-adyacente 2 

gr.insertVertex(grafo, "1")
gr.insertVertex(grafo, "2")
gr.insertVertex(grafo, "3")
gr.addEdge(grafo, "1", "2")

def toString(grafo):
    pass