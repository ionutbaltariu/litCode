from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l = len(coordinates)

        if l == 0 or l == 1:
            return True

        first = coordinates[0]
        last = coordinates[-1]

        # equation of a straight line
        f = lambda x, y: ((x - first[0]) * (last[1] - first[1])) == ((y - first[1]) * (last[0] - first[0]))
        # check if each poin after the first and before the last is on the line
        for i in range(1, len(coordinates) - 1):
            if f(coordinates[i][0], coordinates[i][1]) is False:
                return False

        return True
