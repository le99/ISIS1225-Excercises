import time

def contarTripletasSumaCero(lista):
  """
  Contar 3-tuplas <e1, e2, e3> de elementos en la lista tal que e1 + e2 + e3 sea igual a 0
  Resultado: total de 3-tuplas de elementos cuya suma es 0
  """
  contador = 0
  for i in range(len(lista)):
    for j in range(i+1, len(lista)):
      for k in range(j+1, len(lista)):
        if lista[i]+lista[j]+lista[k] == 0:
          contador += 1
  return contador


N = 5

lista = [x - N/2 for x in range(N)]

t1 = time.process_time()
contarTripletasSumaCero(lista)
t2 = time.process_time()

print(t2-t1) 