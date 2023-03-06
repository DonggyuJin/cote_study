import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

m,n,k = map(int, input().split())
maps = [[0] * n for _ in range(m)]
chk = [[False] * n for _ in range(m)]
for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      maps[i][j] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

cnt = 1
def dfs(y, x):
  global cnt
  for k in range(4):
    ny = y + dy[k]
    nx = x + dx[k]
    if 0 <= ny < m and 0 <= nx < n:
      if maps[ny][nx] == 0 and not chk[ny][nx]:
        chk[ny][nx] = True
        dfs(ny, nx)
        cnt += 1
  return cnt

rs = []
block = 0
for i in range(m):
  for j in range(n):
    if maps[i][j] == 0 and not chk[i][j]:
      chk[i][j] = True
      rs.append(dfs(i, j))
      block += 1
      cnt = 1

rs.sort()
print(block)
print(*rs)