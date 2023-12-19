class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = []

        def dfs(curr_v):
            visited.append(curr_v)
            for v in rooms[curr_v]:
                if v not in visited:
                    dfs(v)

        dfs(0)
        return len(rooms) == len(visited)