import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
result = []
cnt = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
  global cnt
  cnt += 1
  for k in range(4):
    ny = y + dy[k]
    nx = x + dx[k]
    if 0 <= ny < n and 0 <= nx < n:
      if maps[ny][nx] == 1 and chk[ny][nx] == False:
        chk[ny][nx] = True
        dfs(ny, nx)
  return cnt

for i in range(n):
  for j in range(n):
    if maps[i][j] == 1 and chk[i][j] == False:
      chk[i][j] = True
      dfs(i, j)
      result.append(cnt)
      cnt = 0

result.sort()
print(len(result))
print(*result, sep='\n')