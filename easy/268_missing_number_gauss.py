from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 1 - nums[0]

        return length * (length + 1) // 2 - sum(nums)


if __name__ == "__main__":
    print(Solution().missingNumber([1, 2, 3, 4, 5, 6, 0, 8, 9]))
