import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1): graph[i].sort()

def bfs(v):
  q = deque([v])
  visited[v] = 1
  count = 2

  while q:
    v = q.popleft()
    for k in graph[v]:
      if visited[k] == 0:
        q.append(k)
        visited[k] = count
        count += 1

bfs(r)

for i in range(1, n+1): print(visited[i])