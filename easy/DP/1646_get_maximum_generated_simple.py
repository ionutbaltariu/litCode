class Solution:
    # breaks after iterating through n // 2 elements because the array is already populated and all values are known
    # it seems there is no performance improvement
    def getMaximumGenerated(self, n: int) -> int:
        if n in [0, 1]:
            return n

        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        max_val = 0

        for i in range(1, n + 1):
            if 2 <= 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 <= 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
            if max_val < nums[i]:
                max_val = nums[i]

        return max_val


if __name__ == "__main__":
    print(Solution().getMaximumGenerated(4))
