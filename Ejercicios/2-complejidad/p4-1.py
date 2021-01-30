def incognita(n):
  """
  Entender el algoritmo y decir que problema resuelve
  """
  sum = 0
  while n > 0:
    sum += n
    n = n // 2
  return sum

a = incognita(5)
print(a)