n = int(input())

data = [[0 for _ in range(19)] for _ in range(19)]

for i in range(n):
  x, y = map(int, input().split())
  data[x-1][y-1] = 1

for i in range(19):
  for j in range(19):
    print(data[i][j], end=' ')
  print()
