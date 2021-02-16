
def selectionSort (lista, lessfunction):
  """
  Selection sort para una lista generica aplicando la comparación lessfunction
  """
  pos1 = 1
  size = len(lista) - 1

  while pos1 < size:
    minimum = pos1
    # minimun tiene el menor elemento conocido hasta ese momento
    pos2 = pos1 + 1
    while pos2 <= size:
      if lessfunction (lista[pos2],lista[minimum]):
        minimum = pos2 # actualizacion del elemento más pequeño
      
      pos2 += 1
    
    # intercambiar el minimum con el elemento en pos1
    m = lista[minimum]
    lista[minimum] = lista[pos1]
    lista[pos1] = m  
    pos1 += 1


def lessfunction(a, b):
  return a < b

lista = [None,6,4,5,1,2,3]
print(lista)

selectionSort(lista, lessfunction)
print(lista)




