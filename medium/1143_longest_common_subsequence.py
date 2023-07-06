class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # we reached the end (actually start because we're going backwards) of a string
            if i < 0 or j < 0:
                return 0

            # we found two letters that are common, we'll add 1 to the length
            # and keep looking
            if text1[i] == text2[j]:
                advance_in_both = helper(i - 1, j - 1)
                memo[(i - 1, j - 1)] = advance_in_both
                return advance_in_both + 1

            # letters aren't common, we'll advance by one letter in each word and redo the process
            # until we find something common, or we reach the end
            advance_in_first_word = helper(i - 1, j)
            advance_in_second_word = helper(i, j - 1)
            memo[(i - 1, j)] = advance_in_first_word
            memo[(i, j - 1)] = advance_in_second_word
            return max(advance_in_first_word, advance_in_second_word)

        return helper(len(text1) - 1, len(text2) - 1)