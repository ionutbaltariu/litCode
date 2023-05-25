from typing import List

# we first store our seen variables in dict, along with their indexes
# and on every iteration check if the difference from the target and the current value
# can be found in the dict
# if so, return the index from the dict along with the current index


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if (diff := target - num) in seen:
                return [seen[diff], i]

            seen[num] = i


if __name__ == "__main__":
    print(Solution().twoSum([3, 3], 6))