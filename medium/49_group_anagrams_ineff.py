from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for s in strs:
            t_s = ''.join(sorted(s))

            if t_s not in h:
                h[t_s] = [s]
            else:
                h[t_s].append(s)

        return [h.get(key) for key in h]