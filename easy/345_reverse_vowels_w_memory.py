class Solution:
    def reverseVowels(self, s: str) -> str:
        all_vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowels = []
        new_s = []

        for c in s:
            if c in all_vowels:
                vowels.append(c)

        vowels = [vowels[i] for i in range(len(vowels) - 1, -1, -1)]

        j = 0
        for i in range(len(s)):
            if s[i] not in all_vowels:
                new_s.append(s[i])
            else:
                new_s.append(vowels[j])
                j += 1

        return ''.join(new_s)