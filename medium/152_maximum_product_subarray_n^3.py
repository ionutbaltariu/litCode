from math import inf
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = -inf
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                p = 1
                for k in range(i, j + 1):
                    p *= nums[k]
                if p > max_p:
                    max_p = p

        return max_p
