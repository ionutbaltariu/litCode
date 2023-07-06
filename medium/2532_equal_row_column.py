from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counts = {}
        n = len(grid)

        # rows
        for idx, line in enumerate(grid):
            encoded = ','.join([str(x) for x in line])

            if encoded not in counts:
                counts[encoded] = 1
            else:
                counts[encoded] += 1

        count = 0

        for j in range(n):
            encoded = ','.join([str(grid[i][j]) for i in range(n)])

            if encoded in counts:
                count += counts[encoded]

        return count


