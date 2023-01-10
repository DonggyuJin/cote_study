data = [input().split() for _ in range(10)]
x, y = 1, 1
breaks = 0

for i in range(x, 10):
  if breaks == 1:
    break
  for j in range(y, 10):
    if data[i][j] == '2':
      data[i][j] = '9'
      breaks += 1
      break
    if data[i][j] == '0':
      data[i][j] = '9'
    elif data[i][j] == '1':
      x = j-1
      y = j-1
      break

for i in range(10):
  for j in range(10):
    print(data[i][j], end=' ')
  print()
