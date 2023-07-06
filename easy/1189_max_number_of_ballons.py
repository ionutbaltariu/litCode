class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        h = {}
        for c in text:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1

        return min(h.get('b', 0), h.get('a', 0), h.get('l', 0), h.get('o', 0) // 2, h.get('l', 0) // 2, h.get('n', 0))