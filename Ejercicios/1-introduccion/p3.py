import time

t1 = time.process_time()

suma = 0
for i in range(100*1000):
  suma = suma + 1

t2 = time.process_time()

print(t2-t1)