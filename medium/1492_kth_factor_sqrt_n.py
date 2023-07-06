import math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # for each number in (1, sqrt(n)) for which n % i == 0
        # there is a number with which i is multiplied to get n, and that is another factor of n
        # n // i = x -> i * x = n -> n // x = i
        # why sqrt? n = i * x, at most i can be equal to x and equal to the sqrt, resulting in sqrt(n) * sqrt(n) = n
        # one being greater would result in a number that's greater than n
        sq = int(math.sqrt(n))

        for i in range(1, sq + 1):
            if n % i == 0:
                k -= 1

                if not k:
                    return i

        for i in range(sq, 0, -1):
            # skip already processed factor (perfect square number case)
            if i * i == n:
                continue
            if n % (n // i) == 0:
                k -= 1

                if not k:
                    return n // i

        return -1


if __name__ == "__main__":
    print(Solution().kthFactor(12, 3))
