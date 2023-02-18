import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  chs = [[0] * n for _ in range(n)]
  
  currY, currX = map(int, input().split())
  moveY, moveX = map(int, input().split())

  chs[currY][currX] = 1
  
  dy = [-2, -1, 1, 2, 2, 1, -1, -2]
  dx = [1, 2, 2, 1, -1, -2, -2, -1]

  def bfs(y, x):
    q = deque([(y, x)])
    while q:
      ey, ex = q.popleft()
      for k in range(8):
        ny = ey + dy[k]
        nx = ex + dx[k]
        if ey == moveY and ex == moveX:
          print(chs[moveY][moveX]-1)
          return
        if 0 <= ny < n and 0 <= nx < n and chs[ny][nx] == 0:
          chs[ny][nx] = chs[ey][ex] + 1
          q.append((ny, nx))
          
  bfs(currY, currX)