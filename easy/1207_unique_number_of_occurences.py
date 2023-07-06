from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}

        for num in arr:
            if num not in occurences:
                occurences[num] = 1
            else:
                occurences[num] += 1

        total = len(occurences)

        occurences_set = {x for x in occurences.values()}

        return total == len(occurences_set)