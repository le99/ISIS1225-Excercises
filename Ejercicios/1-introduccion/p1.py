import time

a = list(range(1000*1000))
a_len = len(a)


t1 = time.process_time()

b = a.index(a_len -1)
b = a.index(a_len -1)
b = a.index(a_len -1)

t2 = time.process_time()

print(t2-t1)
