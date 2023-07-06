from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorred = 0
        l = len(nums)

        # xor has an absorbing property
        # we first xor all values in the array
        for num in nums:
            xorred ^= num

        # then we xor with every possible value in the given conditions
        # what remains is the missing value, since the others have been "cancelled"
        # e.g:
        # 0b10 ^ 0b10 = 0b00
        for i in range(1, l + 1):
            xorred ^= i

        return xorred


