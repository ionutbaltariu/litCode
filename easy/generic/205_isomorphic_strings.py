class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        if len(s) != len(t):
            return False

        hashtable = {}
        reverse_hashtable = {}

        for i in range(len(s)):
            if s[i] not in hashtable:
                hashtable[s[i]] = t[i]
                if t[i] in reverse_hashtable:
                    if reverse_hashtable[t[i]] != s[i]:
                        return False
                reverse_hashtable[t[i]] = s[i]
            else:

                if hashtable[s[i]] != t[i]:
                    return False

        return True


if __name__ == "__main__":
    print(Solution().isIsomorphic("babc", "baba"))