from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = {}

        if not board:
            return

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == "O":
                    start = i, j
                    q = deque()
                    q.append(start)

                    while q:
                        position = q.popleft()
                        if visited.get(position, False) is True:
                            continue

                        visited[position] = True
                        x, y = position
                        neighbours = []

                        if x != 0:
                            if board[x - 1][y] == "O":
                                neighbours.append((x - 1, y))
                        if x != m - 1:
                            if board[x + 1][y] == "O":
                                neighbours.append((x + 1, y))
                        if y != 0:
                            if board[x][y - 1] == "O":
                                neighbours.append((x, y - 1))
                        if y != n - 1:
                            if board[x][y + 1] == "O":
                                neighbours.append((x, y + 1))

                        for neigh in neighbours:
                            if not visited.get(neigh, False):
                                q.append(neigh)

        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == "O":
                    start = i, j
                    q = deque()
                    q.append(start)

                    while q:
                        position = q.popleft()
                        if visited.get(position, False) is True:
                            continue

                        visited[position] = True
                        x, y = position
                        neighbours = []

                        if x != 0:
                            if board[x - 1][y] == "O":
                                neighbours.append((x - 1, y))
                        if x != m - 1:
                            if board[x + 1][y] == "O":
                                neighbours.append((x + 1, y))
                        if y != 0:
                            if board[x][y - 1] == "O":
                                neighbours.append((x, y - 1))
                        if y != n - 1:
                            if board[x][y + 1] == "O":
                                neighbours.append((x, y + 1))

                        for neigh in neighbours:
                            if not visited.get(neigh, False):
                                q.append(neigh)

        # all the nodes that cannot be converted have been visited
        # the logic is that if an 'O' is connected to an 'O' that lies on the edges
        # of the matrix
        # it will not be converted, same applies for further connected O's. It's like an island.
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"


