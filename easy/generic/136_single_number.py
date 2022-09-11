from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            # xor would eliminate all the duplicates and we'd be left with the single appearance number
            result ^= num
        return result


if __name__ == "__main__":
    print(Solution().singleNumber([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
