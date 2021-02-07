import time

t1 = time.process_time()

n = 0
s = []

lista = []
for i in range(1*1000*1000):
    lista.append(i)

for i in range(1*1000*1000):
  # "string con mucho texto lalal asdf asfd asdf asdf asdf asdf asfasdf afsadf ".split(" ")
  # s.append("a")
  # s.insert(0, "a")
  lista.sort()


t2 = time.process_time()

print(t2-t1)