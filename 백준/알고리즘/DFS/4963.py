import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

while True:
  w,h = map(int, input().split())
  if w == 0 and h == 0: break
  graph = [list(map(int, input().split())) for _ in range(h)]
  chk = [[False] * w for _ in range(h)]
  cnt = 0

  dy = [0, 1, 1, 1, 0, -1, -1, -1]
  dx = [1, 1, 0, -1, -1, -1, 0, 1]
  
  def dfs(y, x):
    for k in range(8):
      ny = y + dy[k]
      nx = x + dx[k]
      if 0 <= ny < h and 0 <= nx < w:
        if graph[ny][nx] == 1 and chk[ny][nx] == False:
          chk[ny][nx] = True
          dfs(ny, nx)

  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1 and chk[i][j] == False:
        chk[i][j] = True
        dfs(i, j)
        cnt += 1
  print(cnt)
        