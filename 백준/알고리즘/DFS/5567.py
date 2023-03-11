import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
chk = [0] * (n+1)
cnt = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1): graph[i].sort()

for i in graph[1]:
  if not chk[i]:
    chk[i] = True
    cnt += 1

  for k in graph[i]:
    if not chk[k]:
      chk[k] = True
      cnt += 1

if not cnt: print(cnt)
else: print(cnt-1)