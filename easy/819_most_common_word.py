from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        forbidden = {'!', '?', "'", ',', ';', '.', ' '}
        banned = set(banned)
        h = {}
        tmp_s = ""

        for c in paragraph:
            if c not in forbidden:
                tmp_s += c.lower()
            else:
                # we can consider that we have a word
                if tmp_s != "":
                    if tmp_s in h:
                        h[tmp_s] += 1
                    else:
                        h[tmp_s] = 1
                tmp_s = ""

        # we can just have a single word
        if tmp_s:
            if tmp_s in h:
                h[tmp_s] += 1
            else:
                h[tmp_s] = 1

        # we're guaranteed to have a result
        # otherwise we can just quit when h is empty
        while True:
            m = max(h, key=h.get)

            if m in banned:
                del h[m]
                continue

            return m