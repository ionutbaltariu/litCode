from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        lst = [[1], [1, 1]]

        for i in range(2, numRows):
            tmp_lst = [1]
            for j in range(1, len(lst[i - 1])):
                tmp_lst.append(lst[i - 1][j - 1] + lst[i - 1][j])
            tmp_lst.append(1)
            lst.append(tmp_lst)
        return lst


if __name__ == "__main__":
    print(Solution().generate(5))
