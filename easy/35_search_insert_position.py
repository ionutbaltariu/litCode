class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # use binary search to search for the value -> o(log(n))
        # if the value isn't found
        # it means that it either should be on the final middle position, or the next one (+1), if the number at that
        # index is smaller
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left+right)//2

            if nums[middle] == target:
                return middle

            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1

        if nums[middle] < target:
            return middle + 1
        else:
            return middle