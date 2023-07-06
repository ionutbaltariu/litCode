from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_val = nums[0]
        while l <= r:
            m = (l + r) // 2

            min_val = min(min_val, nums[m])

            # if our middle is greater than the right value, it means that we're in the part that was rotated
            # (the elements in this part are greater than those that weren't rotated)
            # so our minimum value would surely be on the right part.
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1

        return min_val