import sys
input = sys.stdin.readline

n,k = map(int, input().split())
rs = []
for i in range(1, n+1):
  if n % i == 0: rs.append(i)

if len(rs) < k: print(0)
else: print(rs[k-1])