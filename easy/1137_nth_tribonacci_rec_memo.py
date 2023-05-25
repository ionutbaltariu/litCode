class Solution:
    def __init__(self):
        self.memo = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n in (s := self.memo):
            return s[n]

        self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.memo[n]


if __name__ == "__main__":
    print(Solution().tribonacci(5))
