from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        n = len(grid)
        queue = deque()
        queue.append(((0, 0), [(0, 0)]))
        visited = {(0, 0)}

        if grid[0][0] == 1:
            return -1

        if n == 1 and grid[0][0] == 0:
            return 1

        while queue:
            current, path = queue.popleft()

            if current == (n - 1, n - 1):
                return len(path)

            for d in directions:
                nxt = (current[0] + d[0], current[1] + d[1])

                if nxt[0] < 0 or nxt[0] > n - 1:
                    continue

                if nxt[1] < 0 or nxt[1] > n - 1:
                    continue

                if grid[nxt[0]][nxt[1]] == 0 and nxt not in visited:
                    queue.append((nxt, path + [nxt]))
                    visited.add(nxt)

        return -1
