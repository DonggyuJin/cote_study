import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
count = 1

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(v):
  global count
  visited[v] = count
  graph[v].sort(reverse=True)
  for k in graph[v]:
    if visited[k] == 0:
      count += 1
      dfs(k)

dfs(r)

for i in range(1, n+1): print(visited[i])

"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
result = [0] * (n+1)
count = 1

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n): graph[i].sort()

# print(graph)

def dfs(v):
  global count
  stack = [v]
  while stack:
    node = stack.pop()
    if visited[node] == 1:
      continue
    visited[node] = 1
    result[node] = count
    count += 1
    for k in graph[node]:
      if visited[k] == 0:
        stack.append(k)
  return result

result = dfs(r)
print(*result[1:], sep='\n')
"""