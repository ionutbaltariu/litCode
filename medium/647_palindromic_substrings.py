class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        r = 0

        for i in range(l):
            for j in range(i, l):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    r += 1

        return r