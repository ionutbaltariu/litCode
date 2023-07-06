class Solution:
    def reverseBits(self, n: int) -> int:
        rev, p = 0, 31

        while n != 0:
            rev += (n & 1) * (2 ** p)
            p -= 1
            n >>= 1

        return rev


if __name__ == "__main__":
    print(Solution().reverseBits(1))