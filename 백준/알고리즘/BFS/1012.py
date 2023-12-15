from collections import deque

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    cabbage = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        cabbage[x][y] = 1

    result = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False] * n for _ in range(m)]

    def bfs(x, y):
        visited[x][y] = True
        q = deque()
        q.append((x, y))
        while q:
            curr_x, curr_y = q.popleft()
            for i in range(4):
                nx = curr_x + dx[i]
                ny = curr_y + dy[i]
                if nx >= 0 and nx < m and ny >=0 and ny < n:
                    if cabbage[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

    for i in range(m):
        for j in range(n):
            if cabbage[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                result += 1

    print(result)
