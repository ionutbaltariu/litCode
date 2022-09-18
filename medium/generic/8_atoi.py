class Solution:
    def myAtoi(self, s: str) -> int:
        stripped = s.lstrip()
        negative_number = 1
        subtract = 1

        if not stripped:
            return 0

        if stripped[0] == "0":
            stripped = stripped.lstrip("0")

            if not stripped:
                return 0

            if ord(stripped[0]) < 48 or ord(stripped[0]) > 57:
                return 0

        if stripped[0] == "-":
            negative_number = -1
            subtract = 0
            stripped = stripped[1:]
        elif stripped[0] == "+":
            stripped = stripped[1:]

        if not stripped:
            return 0

        if stripped[0] == "0":
            stripped = stripped.lstrip("0")

            if not stripped:
                return 0

            if ord(stripped[0]) < 48 or ord(stripped[0]) > 57:
                return 0

        idx = 0

        for x in stripped:
            if 47 < ord(x) < 58:
                idx += 1
            else:
                break

        number = stripped[:idx]
        p = len(number) - 1
        returned = 0

        if len(number) > 10:
            return negative_number * 2 ** 31 - subtract

        for x in number:
            returned += pow(10, p) * (ord(x) - 48)
            p -= 1

        if returned >= 2 ** 31:
            return negative_number * 2 ** 31 - subtract

        return negative_number * returned


if __name__ == "__main__":
    print(Solution().myAtoi(" 99w2321set "))
