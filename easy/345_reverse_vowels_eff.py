class Solution:
    def reverseVowels(self, s: str) -> str:
        all_vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        length = len(s)
        l, r = 0, length - 1

        s = list(s)
        while l < r:
            while l < length and s[l] not in all_vowels:
                l += 1

            while r > 0 and s[r] not in all_vowels:
                r -= 1

            if l >= r:
                break

            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return ''.join(s)
