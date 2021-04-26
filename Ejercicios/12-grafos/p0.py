import config
from DISClib.ADT import graph as gr
from DISClib.ADT import list as lt


# Creacion de un grafo no dirigido
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


gr.insertVertex(grafo, "1")
gr.insertVertex(grafo, "2")
gr.addEdge(grafo, "1", "2")


#Imprimir el grafo
for v in lt.iterator(gr.vertices(grafo)):
    print(v)
    adj = gr.adjacents(grafo, v)
    for a in lt.iterator(adj):
        print('-', a)
    
    print()


