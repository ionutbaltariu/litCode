class Solution:
    def reverseWords(self, s: str) -> str:
        first_good_index = 0
        l = len(s)
        first_good_index_rev = l
        string = []

        if l == 0:
            return ""

        # trim trailing and front spaces
        for c in s:
            if c == " ":
                first_good_index += 1
            else:
                break

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                first_good_index_rev -= 1
            else:
                break

        if first_good_index_rev <= first_good_index:
            return ""

        j = -1
        for c in s[first_good_index:first_good_index_rev]:
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