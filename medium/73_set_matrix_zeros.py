from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # will take at most m + n values in the tuples
        pairs = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    pairs.append((i, j))

        for p in pairs:
            for k in range(n):
                matrix[p[0]][k] = 0

            for k in range(m):
                matrix[k][p[1]] = 0


if __name__ == "__main__":
    print(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
