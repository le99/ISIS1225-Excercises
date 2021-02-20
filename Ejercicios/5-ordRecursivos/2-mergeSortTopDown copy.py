def mergeSort (lst, lessfunction):
  lstaux = [None]*len(lst) #crear una lista auxiliar del mismo tamaNo
  sort(lst, lstaux, lessfunction, 1, len(lst)-1)

def sort (lst, auxlst, lessfunction, lo, hi):
  """
  Ordena los elementos de la lista lst que se encuentren en el rango [lo, hi].
  lessfunction es la función de comparación entre los elementos de la lista.
  auxlst es una lista auxiliar del mismo tamaño que la lista original para ayudar al ordenamiento
  """
  if hi <= lo:
    return
  mid = lo + (hi - lo) // 2
  sort(lst, auxlst, lessfunction, lo, mid) #ordenamiento mitad de lst en el rango [lo, mid]
  sort(lst, auxlst, lessfunction, mid+1, hi) #ordenamiento mitad de lst en el rango [mid+1, hi]
  merge(lst, auxlst, lessfunction, lo, mid, hi) #mezcla de las dos mitades ordenadas de lst

def merge(lst, auxlst, lessfunction, lo, mid, hi):
  """
  ordenar el rango [lo, hi] en lst mezclando sus mitades ordenadas en rangos [lo, mid] y [mid+1, hi]
  """
  if hi <= lo:
    return

  #copiar la sublista de lst [lo, hi] a la lista auxlst en el mismo rango  k = lo
  for k in range(lo, hi+1):
    auxlst[k] = lst[k]

  i = lo #recorre la midad ordenada en auxlist en el rango [lo, mid]
  j = mid+1 #recorre la midad ordenada en auxlist en el rango [mid+1, hi]
  
  for k in range(lo, hi+1):
    if i > mid:#ya se pasaron los elementos de la mitad ordenada [lo, mid] a lst
      lst[k] = auxlst[j]
      j += 1
    elif j > hi:#ya se pasaron los elementos de la mitad ordenada [mid+1, hi] a lst
      lst[k] = auxlst[i]
      i += 1
    elif lessfunction(auxlst[j], auxlst[i]):# auxlst[j] < auxlst[i]
      lst[k] = auxlst[j]
      j += 1
    else:
      # auxlst[i] <= auxlst[j]
      lst[k] = auxlst[i]
      i += 1


def lessfunction(a, b):
  return a < b

lista = [None,6,4,5,1,2,3]
print(lista)

mergeSort(lista, lessfunction)
print(lista)


# Based on:
# https://github.com/kevin-wayne/algs4/blob/master/src/main/java/edu/princeton/cs/algs4