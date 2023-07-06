from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maximum = max(arr)

        arr = set(arr)
        current_k = 0
        # if for is never entered
        i = 0
        for i in range(1, maximum+1):
            if i not in arr:
                current_k += 1
            if current_k == k:
                return i

        # means missing number is beyond the existing maximum vlaue
        # we return i (the position we finished the for at)
        # plus the number of missing elements that wasn't covered (k - current_k)
        return i + k - current_k
