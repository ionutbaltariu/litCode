from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = []
        length = len(nums)
        nums.sort()

        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx - 1] == num:
                continue

            l, r = idx + 1, length - 1

            while l < r:
                target_sum = num + nums[l] + nums[r]

                if target_sum == 0:
                    sols.append((num, nums[l], nums[r]))

                    # moving to the next element, filtering duplicates
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif target_sum < 0:
                    l += 1
                else:
                    r -= 1

        return sols