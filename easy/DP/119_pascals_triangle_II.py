from typing import List


class Solution:
    def getRow(self, numRows: int) -> List[int]:
        if numRows == 0:
            return [1]
        if numRows == 1:
            return [1, 1]

        lst = [1, 1]

        for i in range(2, numRows + 1):
            tmp_lst = [1]
            for j in range(1, len(lst)):
                tmp_lst.append(lst[j - 1] + lst[j])
            tmp_lst.append(1)
            lst = tmp_lst

        return lst


if __name__ == "__main__":
    print(Solution().getRow(3))
