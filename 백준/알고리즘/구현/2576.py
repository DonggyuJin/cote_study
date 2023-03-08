import sys
input = sys.stdin.readline

rs = []
for _ in range(7):
  n = int(input())
  if n % 2 != 0 : rs.append(n)

if len(rs)>0:
  print(sum(rs))
  print(min(rs))
else: print(-1)