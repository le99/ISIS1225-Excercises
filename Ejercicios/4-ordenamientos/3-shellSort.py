
def insertionSort(lista, lessfunction):
  """
  shellS sort para una lista generica aplicando la comparación lessfunction
  """
  n = len(lista) - 1
  h = 1
  while h < (n//3): # Se calcula el tamaño del primer gap. La lista se h-ordena con este tamaño
    h = 3*h + 1
    # por ejemplo para n = 100, h toma un valor inicial de 40
  
  while (h >= 1):
    print('h', h)
    for i in range (h+1, n+1): # posiciones validas para comparar con elementos a h-distancia
      j = i
      while (j>=(h+1)) and lessfunction (lista[j],lista[j-h]):
        m = lista[j]
        lista[j] = lista[j-h]
        lista[j-h] = m

        j -= h
    h //= 3 # h se decrementa en un tercio. Si h es 1, se comporta como insertionsort

def lessfunction(a, b):
  return a < b

lista = [None,6,4,5,1,2,3]
print(lista)

insertionSort(lista, lessfunction)
print(lista)




