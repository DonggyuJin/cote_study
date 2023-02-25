import sys
input = sys.stdin.readline

n,k = map(int, input().split())
l = [i for i in range(2, n+1)]
rs = []

def is_prime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
  return True

if n <= 3: print(n)
else:
  for i in range(n-2):
    if len(l) < 1: break
    x = min(l)
    if is_prime(x):
      for j in l:
        if j % x == 0: 
          rs.append(j)
          l.remove(j)
  print(rs[k-1])