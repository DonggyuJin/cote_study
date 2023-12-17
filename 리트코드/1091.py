from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        shortestLen = -1

        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]

        if grid[0][0] !=0 or grid[row-1][col-1] != 0: return shortestLen

        q = deque()
        q.append((0, 0, 1))
        visited[0][0] = True

        dx = [0, 1, 0, -1, 1, 1, -1, -1]
        dy = [1, 0, -1, 0, 1, -1, 1, -1]

        while q:
            cur_r, cur_c, cur_len = q.popleft()
            if cur_r == row-1 and cur_c == col-1:
                shortestLen = cur_len
                break

            for i in range(8):
                nx = cur_r + dx[i]
                ny = cur_c + dy[i]
                if nx >= 0 and nx < row and ny >= 0 and ny < col:
                    if grid[nx][ny] == 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, cur_len+1))

        return shortestLen