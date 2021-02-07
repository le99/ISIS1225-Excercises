import time


def busquedaSecuencialNativo(lista, elemento):
  """
  Busqueda Secuencial/Lineal de un elemento en una lista (recorrido nativo)
  Resultado: Indice en la lista donde se encuentra el elemento. -1 si no se encuentra.
  """
  i = 0
  pos = -1
  for item in lista:
    if item == elemento:
      pos = i
      break
    else:
      i += 1
  return pos


N = 80*1000
lista = [x for x in range(N)]

t1 = time.process_time()
busquedaSecuencialNativo(lista, N/2)
t2 = time.process_time()

print(t2-t1)