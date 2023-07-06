from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0

        for i in range(1, len(nums)):
            # if what we're scanning right now is different from the previous element
            # it means that we should move on the next position and put the different element there
            # j is the index of the "unique element subarray"
            if nums[i] != nums[i - 1]:
                j += 1
                nums[j] = nums[i]

        return j + 1
