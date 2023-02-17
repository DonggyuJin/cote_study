import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  a, b = map(int, input().split())
  c, d = map(int, input().split())
  chess = [[0] * n for _ in range(n)]

  chess[a][b] = 1

  dy = [-2, -1, 1, 2, 2, 1, -1, -2]
  dx = [1, 2, 2, 1, -1, -2, -2 ,-1]
  
  def bfs(y, x):
    q = deque([(y, x)])
    while q:
      ey, ex = q.popleft()
      if ey == c and ex == d:
        print(chess[c][d]-1)
        return
      for k in range(8):
        ny = ey + dy[k]
        nx = ex + dx[k]
        if 0 <= ny < n and 0 <= nx < n and chess[ny][nx] == 0:
          chess[ny][nx] = chess[ey][ex] + 1
          q.append((ny, nx))
  bfs(a, b)