n, cnt = int(input()), 0

while n != 0:
  n //= 5
  cnt += n
  
print(cnt)

"""
from math import factorial as f

n = int(input())
cnt = 0

for i in str(f(n))[::-1]:
  if i != '0': break
  cnt += 1

print(cnt)
"""