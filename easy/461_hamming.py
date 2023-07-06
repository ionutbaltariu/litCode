class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0

        for i in range(32):
            distance += ((x & 1) != (y & 1))
            x >>= 1
            y >>= 1

            if x == 0 and y == 0:
                break

        return distance