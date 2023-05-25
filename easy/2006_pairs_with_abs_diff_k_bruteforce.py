from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        length = len(nums)
        count = 0
        for i in range(length):
            for j in range(i + 1, length):
                if abs(nums[i] - nums[j]) == k:
                    count += 1

        return count


if __name__ == "__main__":
    print(Solution().countKDifference([1, 2, 3, 4, 5, 6, 0, 8, 9], 2))
