import sys
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

maxV = 0

def dfs(y, x, total, cnt):
  global maxV
  if cnt == 4:
    maxV = max(maxV, total)
    return

  for k in range(4):
    ny = y + dy[k]
    nx = x + dx[k]
    if 0 <= ny < n and 0 <= nx < m and not chk[ny][nx]:
      chk[ny][nx] = True
      dfs(ny, nx, total+board[ny][nx], cnt+1)
      chk[ny][nx] = False

# ㅓ, ㅜ, ㅏ, ㅗ
def exception(y, x):
  global maxV
  for k in range(4):
    temp = board[y][x]
    for i in range(3):
      idx = (k + i) % 4
      ny = y + dy[idx]
      nx = x + dx[idx]
      if not (0 <= ny < n and 0 <= nx < m):
        temp = 0
        break
      temp += board[ny][nx]
    maxV = max(maxV, temp)

for i in range(n):
  for j in range(m):
    chk[i][j] = True
    dfs(i, j, board[i][j], 1)
    chk[i][j] = False
    exception(i, j)

print(maxV)