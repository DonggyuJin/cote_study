h, w = map(int, input().split())
n = int(input())

data = [[0 for _ in range(w)] for _ in range(h)]

for i in range(n):
  l, d, x, y = map(int, input().split())
  for j in range(l):
    if d == 0:
      data[x-1][(y-1)+j] = 1
    if d == 1:
      data[(x-1)+j][y-1] = 1

for i in range(h):
  for j in range(w):
    print(data[i][j], end=' ')
  print()
