from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search twice, but continue searching after finding the target value
        # on each left and right parts
        l, r = 0, len(nums) - 1
        first_idx, second_idx = -1, -1

        # leftmost
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                first_idx = m
                # we found a value, but we don't know if it's the leftmost one
                # therefore we just continue updating our right pointer
                # and continue searching in the left subarray
                r = m - 1
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        l, r = 0, len(nums) - 1

        # rightmost
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                second_idx = m
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return [first_idx, second_idx]


if __name__ == "__main__":
    print(Solution().searchRange([0, 1, 1, 1, 4], 1))
