from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        right_sum = sum(nums[1:])
        left_sum = 0
        for i in range(0, len(nums)):
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            if not i + 1 > len(nums) - 1:
                right_sum -= nums[i + 1]
        return -1


if __name__ == "__main__":
    print(Solution().pivotIndex([1,7,3,6,5,6]))
