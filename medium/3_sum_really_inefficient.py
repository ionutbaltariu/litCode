from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = {}
        sols = set()

        pair_is_unique = lambda x, y, z: (x, z, y) not in sols and (z, x, y) not in sols and (z, y, x) not in sols and (
            y, z, x) not in sols and (y, x, z) not in sols

        # the core idea behind this is that we can rewrite a + b + c = 0 as a + b = -c
        # and then our problem transforms into 2sum repeated n times
        # plus the overhead of not adding duplicate combinations
        # O(n*n*5) time complexity
        # and O(n*n) space complexity (hash map created n times that has at most n values)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if (-nums[i] - nums[j]) in h:
                        if pair_is_unique(nums[i], nums[j], -nums[i] - nums[j]):
                            sols.add((nums[i], nums[j], -nums[i] - nums[j]))
                    else:
                        h[nums[j]] = j
            h.clear()

        return sols
