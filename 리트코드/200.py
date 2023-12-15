from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        number_of_islands = 0

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def bfs(x, y):
            visited[x][y] = [True]
            q = deque()
            q.append((x, y))
            while q :
                curr_x, curr_y = q.popleft()
                for i in range(4):
                    nx = curr_x + dx[i]
                    ny = curr_y + dy[i]
                    if nx >= 0 and nx < m and ny >= 0 and ny < n:
                        if grid[nx][ny] == "1" and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    number_of_islands += 1

        return number_of_islands