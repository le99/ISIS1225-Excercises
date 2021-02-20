def quickSort(lst, lessequalfunction):
  sort (lst, 1, len(lst) -1, lessequalfunction)

def sort (lst, lo, hi, lessequalfunction):
  """
  Se localiza el pivot, utilizando la funcion de particion.
  Luego se hace la recursión con los elementos a la izquierda del pivot
  y los elementos a la derecha del pivot
  """
  if (lo >= hi ):
    return
  pivot = partition(lst, lo, hi, lessequalfunction)
  sort(lst, lo, pivot-1, lessequalfunction)
  sort(lst, pivot+1, hi, lessequalfunction)

def partition (lst, lo, hi, lessequalfunction):
  """
  Función que va dejando el pivot en su lugar, mientras mueve elementos menores a la izquierda
  del pivot y elementos mayores a la derecha del pivot
  """
  i = lo
  j = hi + 1
  v = lst[lo]
  while True:
    i += 1
    while lessequalfunction(lst[i], v):
      if i == hi:
        break
      i += 1

    j -= 1
    while lessequalfunction(v, lst[j]):
      if j == lo:
        break
      j -= 1

    if i >= j:
      break
    
    t = lst[i]
    lst[i] = lst[j]
    lst[j] = t

  t = lst[lo]
  lst[lo] = lst[j]
  lst[j] = t
  return j

def lessfunction(a, b):
  return a < b

lista = [None,3,4,5,1,2,6]
print(lista)

quickSort(lista, lessfunction)
print(lista)


# Based on:
https://github.com/kevin-wayne/algs4/blob/master/src/main/java/edu/princeton/cs/algs4/Quick.java