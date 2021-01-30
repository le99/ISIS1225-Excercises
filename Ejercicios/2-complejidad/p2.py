import time
def busquedaMatriz(matriz, filas, columnas, elemento):
  """
  Busqueda de un elemento al recorrer una matriz de filas x columnas elementos
  Resultado: (fila, columna) donde se encuentra el elemento. (-1, -1) si no se encuentra.
  """
  for f in range(filas):
    for c in range(columnas):
      if matriz[f][c] == elemento:
        return f, c

  return -1, -1


F = 200
C = 300

matriz = [[i + j*C for i in range(C)] for j in range(F)]

t1 = time.process_time()
busquedaMatriz(matriz, F, C, F*C/2)
t2 = time.process_time()

print(t2-t1) 