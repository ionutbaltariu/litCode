from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums


if __name__ == "__main__":
    print(Solution().runningSum(list(range(11))))