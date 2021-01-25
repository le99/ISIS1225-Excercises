import time

a = list(range(1000*1000))
a_len = len(a)


t1 = time.process_time()

for i in range(4):
  b = a.index(a_len -1)

t2 = time.process_time()

print(t2-t1)