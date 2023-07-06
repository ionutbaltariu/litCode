class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if not ransomNote or not magazine:
            return False

        h = {}

        for c in magazine:
            if c not in h:
                h[c] = 1
            else:
                h[c] += 1

        for c in ransomNote:
            if c not in h:
                return False
            else:
                h[c] -= 1

        for val in h.values():
            if val < 0:
                return False

        return True
