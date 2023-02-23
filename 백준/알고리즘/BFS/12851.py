import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().split())
chk = [0] * (100001)

rs = 0
cnt = 0

def bfs(v):
  global cnt, rs
  q = deque([v])
  while q:
    v = q.popleft()
    count = chk[v]
    if v == k: 
      rs = count
      cnt += 1
      continue
    for i in (v-1, v+1, 2*v):
      if 0 <= i < 100001:
        if not chk[i] or chk[i] == chk[v]+1:
          chk[i] = count + 1
          q.append(i)

bfs(n)
print(rs, cnt)