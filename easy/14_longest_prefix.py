from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        last = strs[0]

        if not last:
            return ""

        for i in range(1, len(strs)):
            if not strs[i]:
                return ""
            matched_until = 0

            for j in range(min(len(last), len(strs[i]))):
                if strs[i][j] != last[j]:
                    break
                matched_until += 1
            last = strs[i][:matched_until]

        return last


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["Geralt", "George", "Get here!"]))