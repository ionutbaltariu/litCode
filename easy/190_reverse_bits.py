class Solution:
    def reverseBits(self, n: int) -> int:
        rev, p, i = 0, 0, 0
        int_dimension = 32
        bits = [0] * int_dimension

        while n != 0:
            bits[i] = n & 1
            n >>= 1
            i += 1

        for i in range(int_dimension // 2):
            bits[i], bits[int_dimension - i - 1] = bits[int_dimension - i - 1], bits[i]

        for bit in bits:
            if bit & 1:
                rev += 2 ** p
            p += 1
        return rev


if __name__ == "__main__":
    print(Solution().reverseBits(1))