import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v):
  q = deque([v])
  visited[v] = 1
  while q:
    v = q.popleft()
    for k in graph[v]:
      if visited[k] == 0:
        visited[k] = 1
        q.append(k)

for i in range(1, n+1):
  if not visited[i]:
    if not graph[i]:
      cnt += 1
      visited[i] = 1
    else:
      cnt += 1
      bfs(i)

print(cnt)