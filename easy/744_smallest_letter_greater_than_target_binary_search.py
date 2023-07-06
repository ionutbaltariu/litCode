from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # O(log(n)) - binary search
        length = len(letters)
        l, r = 0, length - 1

        while l <= r:
            m = (l + r) // 2

            if letters[m] > target:
                r = m - 1
            else:
                l = m + 1

        # safe since len >= 2
        # if we reach length - 1 there should be two cases
        # we found nothing greater,
        # or we found exactly what's greater
        if m == length - 1:
            if letters[m] <= target:
                return letters[0]
            else:
                return letters[m]

        # then we just have to see where the bigger character would lie, either in the position we finished
        # or the next one
        if letters[m] <= target < letters[m + 1]:
            return letters[m + 1]
        else:
            return letters[m]
