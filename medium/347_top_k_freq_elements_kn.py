from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1

        results = []
        # take the maximum and delete it k times, storing it in the list
        for j in range(k):
            current_max = max(h, key=h.get)
            del h[current_max]
            results.append(current_max)

        return results
