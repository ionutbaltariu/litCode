class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1, h2 = {}, {}

        for c in s:
            if c in h1:
                h1[c] += 1
            else:
                h1[c] = 1

        for c in t:
            if c in h2:
                h2[c] += 1
            else:
                h2[c] = 1

        if len(h1) != len(h2):
            return False

        for k, v in h1.items():
            if k not in h2:
                return False
            else:
                if h2[k] != h1[k]:
                    return False

        return True