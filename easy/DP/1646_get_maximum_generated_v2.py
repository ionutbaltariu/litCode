class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n in [0, 1]:
            return n

        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        max_val = 0

        for i in range(1, n + 1):
            if 2 <= 2 * i <= n:
                s = nums[i]
                nums[2 * i] = nums[i]
                if max_val < s:
                    max_val = s
            if 2 <= 2 * i + 1 <= n:
                s = nums[i] + nums[i + 1]
                nums[2 * i + 1] = s
                if max_val < s:
                    max_val = s

            if i > n // 2:
                break

        return max_val


if __name__ == "__main__":
    print(Solution().getMaximumGenerated(4))
