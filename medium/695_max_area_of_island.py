from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = {}
        m = len(grid)
        n = len(grid[0])
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited.get((i, j), False) is False:
                    current_area = 0
                    bfs_queue = deque()
                    bfs_queue.append((i, j))

                    while len(bfs_queue):
                        position = bfs_queue.popleft()

                        if visited.get(position, False):
                            continue

                        current_area += 1
                        visited[position] = True
                        x, y = position
                        neighbours = []

                        if x != 0:
                            if grid[x - 1][y] == 1:
                                neighbours.append((x - 1, y))
                        if x != m - 1:
                            if grid[x + 1][y] == 1:
                                neighbours.append((x + 1, y))
                        if y != 0:
                            if grid[x][y - 1] == 1:
                                neighbours.append((x, y - 1))
                        if y != n - 1:
                            if grid[x][y + 1] == 1:
                                neighbours.append((x, y + 1))

                        for neigh in neighbours:
                            if not visited.get(neigh, False):
                                bfs_queue.append(neigh)

                    if current_area > max_area:
                        max_area = current_area

        return max_area