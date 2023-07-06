class Solution:
    def reverseBits(self, n: int) -> int:
        rev, p = 0, 31

        while n != 0:
            # |= works because we're just putting bits to the right of the most recent put bit (no overlaps - no losses)
            # 1 << p is equal to 2**p
            rev |= (n & 1) << p
            p -= 1
            n >>= 1

        return rev


if __name__ == "__main__":
    print(Solution().reverseBits(1))