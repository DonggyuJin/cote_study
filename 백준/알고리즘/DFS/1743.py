import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = [[0] * m for _ in range(n)]
chk = [[False] * m for _ in range(n)]
cnt, temp = 1, 1

for _ in range(k):
  r, c = map(int, input().split())
  data[r-1][c-1] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
  
def dfs(y, x):
  global temp
  for k in range(4):
    ny = y + dy[k]
    nx = x + dx[k]
    if 0 <= ny < n and 0 <= nx < m:
      if data[ny][nx] and not chk[ny][nx]:
        chk[ny][nx] = True
        temp += 1
        dfs(ny, nx)
  return temp
  
for i in range(n):
  for j in range(m):
    if data[i][j] and not chk[i][j]:
      chk[i][j] = True
      cnt = max(cnt, dfs(i, j))
      temp = 1
      
print(cnt)