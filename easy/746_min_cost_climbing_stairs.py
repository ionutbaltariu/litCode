from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top of the stairs cost, not included in the original array
        n = len(cost)
        cost.append(0)
        # n + 1 because the top should also be taken into consideration
        dp = [0] * (n + 1)

        # for reaching step 0, we must pay the cost then we can move 1 or to stairs, same for reaching step 1
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            # climbing each step means we have to pay a cost, and we add to that the previous minimum
            # (because we need to get the overall minimum cost at the end)
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return dp[n]