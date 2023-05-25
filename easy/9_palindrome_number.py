class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        copy = x
        mirrored = 0
        while copy != 0:
            mirrored = mirrored * 10 + copy % 10
            copy //= 10

        return mirrored == x


if __name__ == "__main__":
    print(Solution().isPalindrome(123456654321))