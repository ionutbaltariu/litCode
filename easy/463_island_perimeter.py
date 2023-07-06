from collections import deque
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        start = None, None

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start != (None, None):
                break

        bfs_queue = deque()
        bfs_queue.append(start)
        visited = {}
        perimeter = 0

        while len(bfs_queue):
            position = bfs_queue.popleft()

            if visited.get(position, False):
                continue

            visited[position] = True
            i, j = position
            current_perimeter = 4
            neighbours = []

            # each time we encounter a neighbour, a stripe disappears
            # a tile that has all neighbours does not contribute to the perimeter
            if i != 0:
                if grid[i - 1][j] == 1:
                    neighbours.append((i - 1, j))
                    current_perimeter -= 1
            if i != row - 1:
                if grid[i + 1][j] == 1:
                    neighbours.append((i + 1, j))
                    current_perimeter -= 1
            if j != 0:
                if grid[i][j - 1] == 1:
                    neighbours.append((i, j - 1))
                    current_perimeter -= 1
            if j != col - 1:
                if grid[i][j + 1] == 1:
                    neighbours.append((i, j + 1))
                    current_perimeter -= 1

            perimeter += current_perimeter

            for neigh in neighbours:
                if not visited.get(neigh, False):
                    bfs_queue.append(neigh)

        return perimeter
