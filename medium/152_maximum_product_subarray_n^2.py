from math import inf
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = -inf
        n = len(nums)

        for i in range(n):
            # here we're just taking into account that
            # for every iteration of the second loop, we're in fact adding an element to a
            # subarray that starts and index j
            # if we're adding just one element.. then the product can be
            # product_that_was_before * current_element
            p = 1
            for j in range(i, n):
                p *= nums[j]
                max_p = max(p, max_p)
                
        return max_p