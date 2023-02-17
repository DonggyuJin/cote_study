import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
  q = deque([(y, x)])
  while q:
    ey, ex = q.popleft()
    for k in range(4):
      ny = ey + dy[k]
      nx = ex + dx[k]
      if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == 1:
        maze[ny][nx] = maze[ey][ex] + 1
        q.append((ny, nx))
      
  return maze[n-1][m-1]

print(bfs(0,0))