from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1


if __name__ == "__main__":
    print(Solution().search([-1, 0, 3, 5, 9, 12], 13))
