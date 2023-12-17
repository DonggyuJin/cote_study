import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 1
q = deque()
q.append((0, 0, result))

while q:
    cur_x, cur_y, cur_l = q.popleft()

    if cur_x == n-1 and cur_y == m-1:
        result = cur_l
        break

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if miro[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cur_l + 1))
                print(result)

print(result)