import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

bfsVisited = [0] * (n+1)
dfsVisited = [0] * (n+1)

dfsCount = 1

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

print(graph)

def bfs(v):
  q = deque([v])
  bfsVisited[v] = 1
  while q:
    v = q.popleft()
    print(v, end=' ')
    for i in range(1, n+1):
      if bfsVisited[i] == 0 and graph[v][i] == 1:
        q.append(i)
        bfsVisited[i] = 1

def dfs(v):
  dfsVisited[v] = 1
  print(v, end=' ')
  for i in range(1, n+1):
    if dfsVisited[i] == 0 and graph[v][i] == 1: dfs(i)

dfs(v)
print()
bfs(v)