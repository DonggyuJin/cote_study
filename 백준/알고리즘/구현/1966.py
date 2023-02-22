import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  q = list(map(int, range(n)))
  rs = list(map(int, input().split()))
  
  if n == 1: print(1)
  else:
    for i in range(n):
      for j in range(n):
        if rs[i] >= max(rs[i:]): break
        else: 
          rs.append(rs[i])
          rs.pop(i)
          q.append(q[i])
          q.pop(i)
    print(q.index(m)+1)