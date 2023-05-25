class Solution:
    def climbStairs(self, n: int) -> int:
        sol = [0] * (n + 1)
        sol[0] = sol[1] = 1
        for i in range(2, n + 1):
            sol[i] = sol[i - 1] + sol[i - 2]

        return sol[n]


if __name__ == "__main__":
    print(Solution().climbStairs(5))
