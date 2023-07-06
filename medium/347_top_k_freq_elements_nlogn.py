from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1

        # sort descending and return first k elements
        h = sorted(h, key=h.get, reverse=True)

        return h[:k]