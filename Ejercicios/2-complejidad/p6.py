def incognita( lista ):
  """
  Entender el algoritmo y decir que problema resuelve
  """
  i = 0
  j = len(lista) - 1
  while ( i < j ):
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp
    i += 1
    j -= 1