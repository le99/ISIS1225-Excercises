def incognita(n):
  """
  Entender el algoritmo y decir que problema resuelve
  """
  sum = 0
  while n > 0:
    for i in range(n):
      sum += 1
    n = n // 2
  return sum

a = incognita(5)
print(a)