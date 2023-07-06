from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        i, j = 0, length - 1
        final_j = - 1
        final_i = - 1

        while i < len(nums) and j >= 0:
            if nums[j] == target and final_j == -1:
                final_j = j
            if nums[i] == target and final_i == -1:
                final_i = i
            if final_i != -1 and final_j != -1:
                return [final_i, final_j]

            i += 1
            j -= 1

        return [final_i, final_j]
