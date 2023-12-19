n = int(input())
f, s = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = []


for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = 0
def dfs(v, result):
    visited.append(v)

    if v == s: return print(result)
    for nv in graph[v]:
        if nv not in visited:
            dfs(nv, result+1)

dfs(f, result)
if s not in visited: print(-1)