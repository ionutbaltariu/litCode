from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # convert to sets to gain O(1) access time
        s1 = set(nums1)
        s2 = set(nums2)

        ans = [[], []]
        for el in s1:
            if el not in s2:
                ans[0].append(el)
        # ans[0] = [el for el in s1 if el not in s2]

        for el in s2:
            if el not in s1:
                ans[1].append(el)
        # ans[1] = [el for el in s2 if el not in s1]

        return ans