class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([x for x in s if x.isalnum()]).lower()

        i = 0
        l = len(s)

        while i < len(s) / 2:
            if s[i] != s[l - i - 1]:
                return False
            i += 1

        return True
