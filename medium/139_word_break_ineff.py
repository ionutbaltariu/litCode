from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        possibilities = set()

        for word in wordDict:
            if s.startswith(word):
                possibilities.add(word)

        if s in possibilities:
            return True

        while True:
            to_add = set()
            to_remove = set()

            for p in possibilities:
                for word in wordDict:
                    new_s = p + word
                    if s.startswith(new_s):
                        to_add.add(new_s)
                        to_remove.add(p)

            if not to_add or not to_remove:
                break

            possibilities.update(to_add)
            possibilities -= to_remove

        return s in possibilities


if __name__ == "__main__":
    print(Solution().wordBreak("applepenapple", ["apple", "pen", "apple"]))
