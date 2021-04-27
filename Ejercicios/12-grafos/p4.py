import config
from DISClib.ADT import graph as gr
from DISClib.Algorithms.Graphs import dfs
from DISClib.ADT import list as lt

#Ejemplo uso de DFS

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

#DFS
gr.insertVertex(grafo, "a")
gr.insertVertex(grafo, "b")
gr.insertVertex(grafo, "c")
gr.addEdge(grafo, "a", "b")
gr.addEdge(grafo, "c", "b")

search = dfs.DepthFirstSearch(grafo, "b")
path = dfs.pathTo(search, "a")
for v in lt.iterator(path):
  print(v)


