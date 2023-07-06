from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_s = nums[0]
        n = len(nums)

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]

                if s > max_s:
                    max_s = s

        return max_s