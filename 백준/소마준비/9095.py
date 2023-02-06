import sys
from itertools import product
input = sys.stdin.readline

m = int(input())
num = [1,2,3]
for _ in range(m):
  n = int(input())
  result = []
  for i in range(1, n+1):
    result.append(list(product(num, repeat=i)))
  
  count = 0
  for i in range(len(result)):
    for j in range(len(result[i])):
      if sum(result[i][j]) == n: count += 1
  
  print(count)