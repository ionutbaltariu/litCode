# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        bad = 0

        while l <= r:
            m = (l + r) // 2

            if not isBadVersion(m):
                # we search the right part because there cannot be any bad versions before a
                # good version
                l = m + 1
            else:
                # we found a bad version, but we might still find other ones in the left part
                r = m - 1
                bad = m

        return bad

