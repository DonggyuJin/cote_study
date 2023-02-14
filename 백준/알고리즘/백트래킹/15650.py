import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
chk = [False] * (N+1)

def recur(num, idx):
  global k
  if num == M:
    print(' '.join(map(str, result)))
    return
  for i in range(idx, N+1):
    if chk[i] == False:
      chk[i] = True
      result.append(i)
      recur(num+1, i+1)
      chk[i] = False
      result.pop()

recur(0, 1)