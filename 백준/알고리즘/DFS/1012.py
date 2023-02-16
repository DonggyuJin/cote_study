import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  m,n,k = map(int, input().split())
  data = [[0] * m for _ in range(n)]
  chk = [[False] * m for _ in range(n)]
  result = []
  
  for _ in range(k):
    a, b = map(int, input().split())
    data[b][a] = 1

  dy = [0, 1, 0, -1]
  dx = [1, 0, -1, 0]
  
  def dfs(y, x):
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if 0 <= ny < n and 0 <= nx < m:
        if data[ny][nx] == 1 and chk[ny][nx] == False:
          chk[ny][nx] = True
          dfs(ny, nx)
  
  for i in range(n):
    for j in range(m):
      if data[i][j] == 1 and chk[i][j] == False:
        chk[i][j] = True
        dfs(i, j)
        result.append(1)
        
  print(len(result))