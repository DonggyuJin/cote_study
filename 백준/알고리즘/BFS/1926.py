import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
  rs = 1
  q = deque()
  q.append((y,x))
  while q:
    ey, ex = q.popleft()
    for k in range(4):
      ny = ey + dy[k]
      nx = ex + dx[k]
      if 0 <= ny < n and 0 <= nx < m:
        if map[ny][nx] == 1 and chk[ny][nx] == False:
          chk[ny][nx] = True
          rs += 1
          q.append((ny, nx))
  return rs

count = 0
maxNum = 0
for i in range(n):
  for j in range(m):
    if map[i][j] == 1 and chk[i][j] == False:
      chk[i][j] = True
      count += 1
      maxNum = max(maxNum, bfs(i, j))

print(count)
print(maxNum)