class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}

        for c in s:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1

        for c in t:
            if c in h:
                h[c] -= 1

                if h[c] < 0:
                    return False
            else:
                return False

        return True if sum(h.values()) == 0 else False