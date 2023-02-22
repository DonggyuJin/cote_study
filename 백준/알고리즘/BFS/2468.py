import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x, maxV):
  q = deque([(y, x)])
  chk[y][x] = True
  while q:
    ey, ex = q.popleft()
    for k in range(4):
      ny = ey + dy[k]
      nx = ex + dx[k]
      if 0 <= ny < n and 0 <= nx < n and not chk[ny][nx] and maps[ny][nx] > maxV:
        chk[ny][nx] = True
        q.append((ny, nx))

cnt = 0
for i in range(max(map(max, maps))):
  chk = [[False] * n for _ in range(n)]
  minV = 0
  
  for y in range(n):
    for x in range(n):
      if not chk[y][x] and maps[y][x] > i:
        bfs(y, x, i)
        minV += 1

  cnt = max(cnt, minV)
  
print(cnt)

"""
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x, maxV):
  q = deque([(y, x)])
  while q:
    ey, ex = q.popleft()
    for k in range(4):
      ny = ey + dy[k]
      nx = ex + dx[k]
      if 0 <= ny < n and 0 <= nx < n:
        if maps[ny][nx] > maxV and not chk[ny][nx]:
          chk[ny][nx] = True
          q.append((ny, nx))

maxV = 0
for i in range(n):
  maxV = max(maxV, max(maps[i]))

cnt = 0
for i in range(maxV):
  chk = [[False] * n for _ in range(n)]
  minV = 0
  
  for y in range(n):
    for x in range(n):
      if maps[y][x] > i and not chk[y][x]:
        bfs(y, x, i)
        minV += 1

  if cnt < minV:
    cnt = minV
  
print(cnt)
"""