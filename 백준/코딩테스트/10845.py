import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
result = deque([])
for _ in range(n):
  l = len(result)
  command = input().rstrip()

  if 'push' in command:
    text = command.split()[1]
    result.append(text)
  if 'pop' == command:
    if l > 0: 
      print(result[0])
      result.popleft()
    else: print(-1)
  if 'size' == command:
    print(l)
  if 'empty' == command:
    if l == 0: print(1)
    else: print(0)
  if 'front' == command:
    if l > 0: print(result[0])
    else: print(-1)
  if 'back' == command:
    if l > 0: print(result[-1])
    else: print(-1)