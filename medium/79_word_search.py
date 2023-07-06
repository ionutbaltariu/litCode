from collections import deque
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        start_positions = set()

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start_positions.add((i, j))
        visited = {}
        print(start_positions)
        for start in start_positions:
            q = deque()
            q.append(start)
            k = 1

            while q:
                if k >= len(word):
                    return True
                position = q.popleft()

                if visited.get(position, False) is True:
                    continue

                visited[position] = True
                x, y = position
                neighbours = []

                if x != 0:
                    if board[x - 1][y] == word[k]:
                        neighbours.append((x - 1, y))
                if x != m - 1:
                    if board[x + 1][y] == word[k]:
                        neighbours.append((x + 1, y))
                if y != 0:
                    if board[x][y - 1] == word[k]:
                        neighbours.append((x, y - 1))
                if y != n - 1:
                    if board[x][y + 1] == word[k]:
                        neighbours.append((x, y + 1))

                k += 1

                for neigh in neighbours:
                    if not visited.get(neigh, False):
                        q.append(neigh)

        return False


if __name__ == "__main__":
    print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCE"))
