import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
pict = [list(map(str, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x, color):
  q = deque([(y, x)])
  while q:
    ey, ex = q.popleft()
    for k in range(4):
      ny = ey + dy[k]
      nx = ex + dx[k]
      if 0 <= ny < n and 0 <= nx < n:
        if pict[ny][nx] == color and chk[ny][nx] == False:
          chk[ny][nx] = True
          q.append((ny, nx))

# 적록색약이 아닌 사람
counts = {'R': 0, 'G': 0, 'B': 0}
for i in range(n):
  for j in range(n):
    if pict[i][j] in counts and not chk[i][j]:
      chk[i][j] = True
      bfs(i, j, pict[i][j])
      counts[pict[i][j]] += 1

cntR, cntG, cntB = counts['R'], counts['G'], counts['B']

print(cntR+cntG+cntB, end=' ')

# 적록색약인 사람
chk = [[False] * n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if pict[i][j] == 'G':
      pict[i][j] = 'R'

counts = {'R': 0, 'B': 0}
for i in range(n):
  for j in range(n):
    if pict[i][j] in counts and not chk[i][j]:
      chk[i][j] = True
      bfs(i, j, pict[i][j])
      counts[pict[i][j]] += 1

cntR, cntB = counts['R'], counts['B']

print(cntR+cntB)