from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zeros = 0
        for num in nums:
            if num != 0:
                p *= num
            else:
                zeros += 1

        if zeros == 0:
            result = []

            for num in nums:
                result.append(p // num)

            return result
        if zeros == 1:
            result = []

            for num in nums:
                if num != 0:
                    result.append(0)
                else:
                    result.append(p)

            return result

        if zeros > 1:
            return [0] * len(nums)
