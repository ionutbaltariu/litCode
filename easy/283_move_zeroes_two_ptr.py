class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # j will increase when finding a non-zero number, and it will represent the index at which to move one
        j = 0
        l = len(nums)

        for i in range(l):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1

        # overwrite with zeroes after the last non-zero moved digit
        if j < l:
            for i in range(j - 1, len(nums)):
                nums[j] = 0

        return nums
