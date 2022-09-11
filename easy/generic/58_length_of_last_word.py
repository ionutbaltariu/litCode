class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0
        stripped = s.rstrip()

        for i in range(len(stripped) - 1, -1, -1):
            if stripped[i] != " ":
                last_word_length += 1
            else:
                break

        return last_word_length


if __name__ == "__main__":
    print(Solution().lengthOfLastWord(" asd a ds qw  qww er z f ffffffff      "))