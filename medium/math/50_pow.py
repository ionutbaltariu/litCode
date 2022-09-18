class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = x

        if x == 0:
            return 0

        if n == 0 or x == 1:
            return 1

        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1

        was_negative = False

        if n < 0:
            was_negative = True
            n *= -1

        for i in range(n - 1):
            x *= p

            if x == 0 or 1 / x == 0:
                break

        if was_negative:
            return 1 / x
        else:
            return x


if __name__ == "__main__":
    print(Solution().myPow(-1, 10000001))
