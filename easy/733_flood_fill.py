from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = {}

        if image[sr][sc] == color:
            return image

        bfs_queue = deque()
        bfs_queue.append((sr, sc))
        m = len(image)
        n = len(image[0])
        what_will_change = image[sr][sc]

        while len(bfs_queue):
            position = bfs_queue.popleft()

            if visited.get(position, False):
                continue

            visited[position] = True
            i, j = position
            image[i][j] = color
            neighbours = []

            if i != 0:
                if image[i - 1][j] == what_will_change:
                    neighbours.append((i - 1, j))
            if i != m - 1:
                if image[i + 1][j] == what_will_change:
                    neighbours.append((i + 1, j))
            if  j != 0:
                if image[i][j - 1] == what_will_change:
                    neighbours.append((i, j - 1))
            if j != n - 1:
                if image[i][j + 1] == what_will_change:
                    neighbours.append((i, j + 1))

            for neigh in neighbours:
                if not visited.get(neigh, False):
                    bfs_queue.append(neigh)

        return image