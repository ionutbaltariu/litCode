from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)

        if l == 0 or l == 1:
            return l

        current = 1
        overall = 0

        for i in range(1, l):
            if nums[i] == nums[i - 1] + 1:
                current += 1
            elif nums[i] != nums[i - 1]:
                current = 1
            overall = max(current, overall)

        return overall
