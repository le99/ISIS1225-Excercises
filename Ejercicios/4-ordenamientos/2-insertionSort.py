
def insertionSort(lista, lessfunction):
  """
  Insertion sort para una lista genérica aplicando la comparación lessfunction  """
  size = len(lista) -1
  pos1 = 1
  while pos1 <= size:
    pos2 = pos1
    while (pos2 >1) and lessfunction(lista[pos2],lista[pos2-1]):
      #Intercambiar elementos
      m = lista[pos2]
      lista[pos2] = lista[pos2 -1]
      lista[pos2 - 1] = m 
      pos2 -= 1
    pos1 += 1

def lessfunction(a, b):
  return a < b

lista = [None,3,1,2]
print(lista)

insertionSort(lista, lessfunction)
print(lista)




