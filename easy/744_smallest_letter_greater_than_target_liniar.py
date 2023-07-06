from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # O(N) - liniar scan

        for l in letters:
            if ord(l) > ord(target):
                return l

        return letters[0]