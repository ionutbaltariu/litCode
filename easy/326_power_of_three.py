from math import log10


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        l = log10(n) / log10(3)

        return l == float(int(l))