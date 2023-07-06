from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {
            order[i]: i for i in range(len(order))
        }

        for i in range(len(words) - 1):
            j = 0
            current_word_length = len(words[i])
            next_word_length = len(words[i + 1])

            while j < min(current_word_length, next_word_length):
                if words[i][j] != words[i + 1][j]:
                    break
                else:
                    j += 1

            if current_word_length == next_word_length == j:
                if words[i][j - 1] != words[i + 1][j - 1]:
                    return False
                else:
                    continue

            if j == next_word_length and j < current_word_length:
                return False

            if order[words[i][j]] > order[words[i + 1][j]]:
                return False

        return True


if __name__ == "__main__":
    # print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    # print(Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
    print(Solution().isAlienSorted(["hello","hello"], "abcdefghijklmnopqrstuvwxyz"))