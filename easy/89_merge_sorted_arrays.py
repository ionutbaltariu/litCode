from typing import List


# go from last elements (which are the biggest in both arrays)
# while there are elements in either nums1 or nums2
# put the biggest one in nums1 at the i+j+1 index
# decrease the index of the array that held the biggest element
# if there are any remaining elements in nums1, nothing should be done because the result should be put in nums1
# and the remaining elements are the smallest
# if there are any remaining elements in nums2, overwrite the existing elements in nums1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1

        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            else:
                nums1[i + j + 1] = nums1[i]
                i -= 1

        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1

        print(nums1)


if __name__ == '__main__':
    Solution().merge([1, 3, 7, 0, 0, 0], 3, [4, 5, 6], 3)
