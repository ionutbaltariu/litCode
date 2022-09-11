class Solution:
    def __init__(self):
        self.memo = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in (s := self.memo):
            return s[n]
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]


if __name__ == "__main__":
    print(Solution().fib(64))
