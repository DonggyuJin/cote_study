import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n): graph[i].sort()

def dfs(v):
  visited[v] = 1
  for k in graph[v]:
    if visited[k] == 0:
      dfs(k)

dfs(1)
print(sum(visited)-1)

"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n): graph[i].sort()

def dfs(v):
  global count
  visited[v] = count
  for k in graph[v]:
    if visited[k] == 0:
      count += 1
      dfs(k)

dfs(1)
rs = [i for i in visited if i not in {0}]
print(len(rs)-1)
"""