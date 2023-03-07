import sys
input = sys.stdin.readline

result = []
for i in range(4):
  a, b = map(int, input().split())
  if i == 0:
    result.append(b)
  elif i == 1 or i == 2:
    result.append(result[i-1]-a+b)
  else:
    result.append(result[i-1]-a)
print(max(result))