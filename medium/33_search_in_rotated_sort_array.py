from math import inf
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l, r = 0, length - 1
        min_val = inf
        pivot_idx = - 1

        # the idea is the following: find the pivot (the index where the array would actually begin)
        # binary search what's before the pivot (rotated part, still ordered)
        # then binary search what's from the pivot to the end of the array (normal part)

        while l <= r:
            m = (l + r) // 2

            if nums[m] < min_val:
                min_val = nums[m]
                pivot_idx = m

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        l, r = 0, pivot_idx

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        l, r = pivot_idx, length - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return -1