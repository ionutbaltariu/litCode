class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}

        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                return num