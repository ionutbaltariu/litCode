class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        for i in range(1, n + 1):
            digit_sum = 0
            while i != 0:
                digit_sum += i % 10
                i //= 10
            if digit_sum not in groups:
                groups[digit_sum] = 1
            else:
                groups[digit_sum] += 1

        values = groups.values()
        max_group_size = max(values)
        max_size_groups = [x for x in values if x == max_group_size]

        return len(max_size_groups)


if __name__ == "__main__":
    print(Solution().countLargestGroup(133))
