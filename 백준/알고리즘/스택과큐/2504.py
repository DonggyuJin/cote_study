import sys
input = sys.stdin.readline

brack = list(input().strip())
array = []
rs, temp = 0, 1

for i in range(len(brack)):
  if brack[i] == '(':
    array.append(brack[i])
    temp *= 2
  elif brack[i] == '[':
    array.append(brack[i])
    temp *=3
  elif brack[i] == ')':
    if not array or array[-1] == '[':
      rs = 0
      break
    if brack[i-1] == '(':
      rs += temp
    array.pop()
    temp //= 2
  else:
    if not array or array[-1] == '(':
      rs = 0
      break
    if brack[i-1] == '[':
      rs += temp
    array.pop()
    temp //= 3

if array: print(0)
else: print(rs)