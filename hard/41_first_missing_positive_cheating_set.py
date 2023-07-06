from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)

        i = 0
        for i in range(1, max(nums) + 1):
            if i not in nums:
                return i

        return i + 1