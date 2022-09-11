from math import log, floor


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        pos_max = 2147483647
        neg_min = -2147483648

        y = 0
        flag = True if x < 0 else False

        # we'll work with the positive number and just change sign at the end
        if flag is True:
            x *= -1

        idx = floor(log(x, 10))

        while x != 0:
            expr = (x % 10) * pow(10, idx)
            # overflow: a + b > pos_max <=> a > pos_max - b
            # underflow a + b < neg_min <=> a < neg_min + b (b should be POSITIVE)
            # underflow if a is negative: a + b < neg_min <=> b < neg_min - a
            if not flag:
                if y > pos_max - expr:
                    return 0
            else:
                if expr < neg_min + y:
                    return 0

            y += expr
            x //= 10
            idx -= 1

        return y if flag is not True else -1 * y


if __name__ == "__main__":
    print(Solution().reverse(-2147483648))
