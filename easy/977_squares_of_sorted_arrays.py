from typing import List


# split in two lists (negative and positive)
# reverse the negative one
# merge sort

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums1, nums2 = [], []
        m, total = 0, 0

        for el in nums:
            total += 1
            if el >= 0:
                nums1.append(el * el)
                m += 1

        if m == 0:
            return [nums[i] * nums[i] for i in range(total - 1, -1, -1)]

        n = total - m

        if n == 0:
            return nums1

        nums2 = [nums[i] * nums[i] for i in range(n - 1, -1, -1)]

        for i in range(m, total):
            nums1.append(0)

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

        return nums1


if __name__ == "__main__":
    print(Solution().sortedSquares([-10000, -9999, -7, -5, 0, 0, 10000]))
