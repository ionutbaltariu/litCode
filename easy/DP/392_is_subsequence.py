class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subsequence_length = len(s)
        sequence_length = len(t)

        if not subsequence_length:
            return True
        if not sequence_length:
            return False
        if subsequence_length > sequence_length:
            return False

        idx = 0
        for l in t:
            if l == s[idx]:
                idx += 1
                if idx == subsequence_length:
                    return True

        return False


if __name__ == "__main__":
    print(Solution().isSubsequence("test", "i am testing algorithms"))
