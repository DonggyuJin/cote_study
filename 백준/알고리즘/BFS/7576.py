import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
tom = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

q = deque([])

for i in range(n):
  for j in range(m):
    if tom[i][j] == 1:
      q.append((i, j))

def bfs():
  while q:
    ey, ex = q.popleft()
    for k in range(4):
      ny = ey + dy[k]
      nx = ex + dx[k]
      if 0 <= ny < n and 0 <= nx < m and tom[ny][nx] == 0:
          tom[ny][nx] = tom[ey][ex] + 1
          q.append((ny, nx))

bfs()
for i in tom:
  for j in i:
    if j == 0: 
      print(-1)
      exit(0)
  cnt = max(cnt, max(i))

print(cnt-1)