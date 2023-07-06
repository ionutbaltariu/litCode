from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        # base cases
        # maximum money we can get at house 1 is robbing house 1
        dp[0] = nums[0]
        # maximum money we can get at house 2 is robbing house 2 (we cannot rob house 2 and house 1) or robbing house 1
        dp[1] = max(nums[0], nums[1])

        # then the maximum will be:
        # maximum at house 3 can either be only robbing house 2 (already known), or robbing house 1 (already known) and house 3 (taken from 'nums')
        # ..
        # maximum at house n can either be robbing house n - 1 (calculated) or borring house n - 2 (calculated) and house n (known cost)

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]