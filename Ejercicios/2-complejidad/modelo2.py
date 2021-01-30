import time

t1 = time.process_time()

n = 0
s = []
for i in range(1*1000*1000):
  # "string con mucho texto lalal asdf asfd asdf asdf asdf asdf asfasdf afsadf ".split(" ")
  # s.append("a")
  # s.insert(0, "a")

t2 = time.process_time()

print(t2-t1)