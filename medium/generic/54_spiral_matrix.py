from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = top = 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        spiraled = []
        while left <= right and top <= bottom:
            # traverse upper line
            for i in range(left, right + 1):
                spiraled.append(matrix[top][i])
            top += 1

            # traverse right column
            for i in range(top, bottom + 1):
                spiraled.append(matrix[i][right])
            right -= 1

            if left > right or top > bottom:
                break

            # traverse the bottom line in reverse
            for i in range(right, left - 1, -1):
                spiraled.append(matrix[bottom][i])
            bottom -= 1

            # traverse the left column in reverse
            for i in range(bottom, top - 1, -1):
                spiraled.append(matrix[i][left])

            left += 1
        return spiraled


if __name__ == "__main__":
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
