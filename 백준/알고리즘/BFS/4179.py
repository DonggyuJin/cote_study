import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
maze = []
fire_q, esca_q = deque(), deque()
fire, escape = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]

for i in range(R):
  maze.append(list(input().strip()))
  for j in range(C):
    if maze[i][j] == "J":
      esca_q.append((i, j))
      escape[i][j] = 1
    elif maze[i][j] == "F":
      fire_q.append((i, j))
      fire[i][j] = 1
          
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def fireBfs():
  while fire_q:
    y, x = fire_q.popleft()
    for d in range(4):
      ny = y + dy[d]
      nx = x + dx[d]
      if not (0 <= ny < R and 0 <= nx < C):
        continue
      if maze[ny][nx] == "#" or fire[ny][nx]:
        continue
      fire[ny][nx] = fire[y][x] + 1
      fire_q.append((ny, nx))

def escaBfs():
  while esca_q:
    y, x = esca_q.popleft()
    for d in range(4):
      ny = y + dy[d]
      nx = x + dx[d]
      if not (0 <= ny < R and 0 <= nx < C):
        print(escape[y][x])
        return
      if escape[ny][nx] or maze[ny][nx] == "#":
        continue
      if fire[ny][nx] and escape[y][x] + 1 >= fire[ny][nx]:
        continue
      escape[ny][nx] = escape[y][x] + 1
      esca_q.append((ny, nx))
  print("IMPOSSIBLE")
  return

fireBfs()
escaBfs()