class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n in [1, 2]:
            return 1

        t0 = 0
        t1 = t2 = 1

        for i in range(3, n):
            t0, t1, t2 = t1, t2, t0 + t1 + t2

        return t0 + t1 + t2


if __name__ == "__main__":
    print(Solution().tribonacci(5))
