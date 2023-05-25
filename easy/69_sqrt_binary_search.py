class Solution:
    def mySqrt(self, x: int) -> int:
        left = 2
        right = x

        if left > right:
            return x

        middle = 0

        while left <= right:
            middle = (left + right) // 2
            if middle * middle == x:
                return middle

            if middle * middle < x:
                left = middle + 1
            else:
                right = middle - 1

        if middle * middle < x:
            return middle
        else:
            return middle - 1


if __name__ == "__main__":
    print(Solution().mySqrt(4))
