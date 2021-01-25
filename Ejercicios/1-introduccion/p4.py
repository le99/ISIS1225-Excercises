import time

t1 = time.process_time()

numeros = []

for i in range(1000*1000):
  numeros.insert(0, i)

t2 = time.process_time()

print(t2-t1)


#https://docs.python.org/3/faq/design.html#how-are-lists-implemented-in-cpython