import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
result = deque([])
for _ in range(n):
  cmd = input()
  if 'push' in cmd:
    pushs = list(cmd.split())
    result.append(pushs[1])
  if 'pop' in cmd:
    if len(result) == 0: print(-1)
    else:
      print(result[0])
      result.popleft()
  if 'size' in cmd: print(len(result))
  if 'empty' in cmd:
    if len(result) == 0: print(1)
    else: print(0)
  if 'front' in cmd:
    if len(result) == 0: print(-1)
    else: print(result[0])
  if 'back' in cmd:
    if len(result) == 0: print(-1)
    else: print(result[-1])