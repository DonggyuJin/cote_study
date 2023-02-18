import sys
from collections import deque

n,k = map(int, input().split())
chk = [0] * (100001)

def bfs(v):
  q = deque([v])
  while q:
    v = q.popleft()
    if v == k: return chk[v]
    for i in (v-1, v+1, 2*v):
      if 0 <= i < 100001 and not chk[i]:
        chk[i] = chk[v] + 1
        q.append(i)

print(bfs(n))