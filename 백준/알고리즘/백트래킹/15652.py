import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def recur(num, idx):
  if num == M:
    print(' '.join(map(str, result)))
    return
  for k in range(idx, N+1):
      result.append(k)
      recur(num+1, k)
      idx += 1
      result.pop()

recur(0, 1)