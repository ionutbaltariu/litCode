class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = -1
        max_palindrome = None
        l = len(s)

        for i in range(l):
            for j in range(i, l):
                if (p := s[i:j + 1]) == s[i:j + 1][::-1]:
                    if j - i > max_len:
                        max_palindrome = p
                        max_len = j - i

        return max_palindrome
