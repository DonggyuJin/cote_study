data = [input().split() for _ in range(19)]
n = int(input())

for i in range(n):
  x, y = map(int, input().split())
  for j in range(19):
    if data[x-1][j] == '0':
      data[x-1][j] = '1'
    else:
      data[x-1][j] = '0'
    if data[j][y-1] == '1':
      data[j][y-1] = '0'
    else:
      data[j][y-1] = '1'

for i in range(19):
  for j in range(19):
    print(data[i][j], end=' ')
  print()
