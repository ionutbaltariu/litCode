class Solution:
    def partitionString(self, s: str) -> int:
        temp_set = set()
        k = 0
        for c in s:
            print(c)
            if c not in temp_set:
                temp_set.add(c)
            else:
                print(temp_set)
                temp_set.clear()
                temp_set.add(c)
                k += 1

        if len(temp_set):
            k += 1

        return k

if __name__ == "__main__":
    print(Solution().partitionString("ababab"))