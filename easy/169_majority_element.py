from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1

        return max(h, key=h.get)