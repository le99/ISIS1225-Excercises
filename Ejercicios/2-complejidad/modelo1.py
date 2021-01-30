import time

t1 = time.process_time()

n = 0
for i in range(1*1000*1000):
  # n = n + 1
  # n = n - 1
  # n = n * 2
  # n = n / 2
  # n = 3

t2 = time.process_time()

print(t2-t1)