from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(0, n + 1):
            num = 0
            while i != 0:
                if i & 1:
                    num += 1
                i >>= 1
            lst.append(num)
        return lst


if __name__ == "__main__":
    # it hints that there could be a O(n) solution
    print(Solution().countBits(5))
