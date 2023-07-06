from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        # we're guaranteed to have at least 2 elems

        difference = arr[0] - arr[1]

        for i in range(1, len(arr) - 1):
            current_diff = arr[i] - arr[i + 1]

            if current_diff != difference:
                return False

        return True