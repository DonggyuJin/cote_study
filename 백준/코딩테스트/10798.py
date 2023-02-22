import sys
input = sys.stdin.readline

text = []
for _ in range(5):
  text.append(list(map(str, input().strip())))

maxs = 0
for i in range(5):
  maxs = max(maxs, len(text[i]))

for i in range(5):
  while len(text[i]) < maxs:
    text[i].append(' ')

rs = ''
for i in range(maxs):
  for j in range(5):
    rs += text[j][i]

rs = rs.replace(' ', '')
print(rs)