from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for (idx, num) in enumerate(nums):
            for (jdx, tmp) in enumerate(nums):
                if idx != jdx and num + tmp == target:
                    return [idx, jdx]


if __name__ == "__main__":
    print(Solution().twoSum([1, 2, 3, 4, 9, 5], 9))
