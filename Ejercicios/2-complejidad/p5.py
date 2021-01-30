import time

def busquedaBinaria(listaOrdenada, elemento):
  """
  Busqueda Binaria de un elemento en una lista ordenada ascendentemente
  Resultado: Indice en la lista donde se encuentra el elemento. -1 si no se encuentra.
  """
  i = 0
  f = len(listaOrdenada) - 1
  pos = -1
  encontro = False
  while i <= f and not encontro:
    # calcular la posicion de la mitad entre i y f
    m = (i + f) // 2
    if listaOrdenada[m] == elemento:
      pos = m
      encontro = True
    elif listaOrdenada[m] > elemento:
      f = m - 1
    else:
      i = m + 1
  return pos

N = 10
lista = [x for x in range(10)]

t1 = time.process_time()
b = busquedaBinaria(lista, N/2)
t2 = time.process_time()

print(t2-t1) 
