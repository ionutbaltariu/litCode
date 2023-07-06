class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0

        # either x or y should be greater than 0, but if we reach one zero we should stop
        while (x | y) > 0:
            distance += ((x & 1) != (y & 1))
            x >>= 1
            y >>= 1

            if (x << 1) == 0 or (y << 1) == 0:
                break

        return distance