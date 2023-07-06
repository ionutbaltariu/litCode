class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # use dict, compare keys
        # if keys are diff, it's impossible to get one str from the other
        # then compare values -> cannot do by using set because the values aren't and shouldn't be unique
        # so just sort and then compare ony by one

        len1 = len(word1)
        len2 = len(word2)

        if len1 != len2:
            return False

        occ1 = {}
        occ2 = {}

        for c in word1:
            if c not in occ1:
                occ1[c] = 1
            else:
                occ1[c] += 1

        for c in word2:
            if c not in occ2:
                occ2[c] = 1
            else:
                occ2[c] += 1

        keys1 = set(occ1.keys())
        keys2 = set(occ2.keys())

        if len(keys1) != len(keys2):
            return False

        if keys1 != keys2:
            return False

        vals1 = occ1.values()
        vals2 = occ2.values()

        # prob redundant
        if len(vals1) != len(vals2):
            return False

        vals1 = sorted(vals1)
        vals2 = sorted(vals2)

        for i in range(len(vals1)):
            if vals1[i] != vals2[i]:
                return False

        return True


