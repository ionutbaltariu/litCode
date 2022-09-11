class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        f0 = f1 = 1

        for i in range(2, n - 1):
            f1, f0 = f0 + f1, f1

        return f0 + f1


if __name__ == "__main__":
    print(Solution().fib(64))
