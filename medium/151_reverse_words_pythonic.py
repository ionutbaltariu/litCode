class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        string = []

        if len(s) == 0:
            return ""

        # trim trailing and front spaces

        j = -1
        for c in s:
            if c != " ":
                string.append(c)
                j += 1
            else:
                if string[j] != " ":
                    string.append(c)
                    j += 1

        return ' '.join(''.join(string).split()[::-1])


if __name__ == "__main__":
    print(Solution().reverseWords("  a     blue  a  sky   "))
