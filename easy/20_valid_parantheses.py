from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) == 1:
            return False

        matches = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        q = deque()

        for c in s:
            if c in matches:
                q.append(c)
            else:
                # if we remain without open parentheses
                if not q:
                    return False

                # if the current closed parenthesis doesn't math the last opened one
                if c != matches[q.pop()]:
                    return False

        # if there were more opened parentheses than closed ones
        if q:
            return False

        return True


if __name__ == "__main__":
    print(Solution().isValid("{({({({({{{{{{{({[[]]})}}}}}}})})})})([])}()"))