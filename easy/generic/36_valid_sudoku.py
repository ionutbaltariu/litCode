from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # lines

        for i in range(9):
            tmp_lst = [x for x in board[i] if x != "."]
            if len(set(tmp_lst)) != len(tmp_lst):
                return False

        for j in range(9):
            tmp_lst = []
            for i in range(9):
                if (b := board[i][j]) != ".":
                    tmp_lst.append(b)
            if len(set(tmp_lst)) != len(tmp_lst):
                return False

        for k1 in [0, 1, 2]:
            for k2 in [0, 1, 2]:
                tmp_lst = []
                for i in range(k1 * 3, (k1 + 1) * 3):
                    for j in range(k2 * 3, (k2 + 1) * 3):
                        if (b := board[i][j]) != ".":
                            tmp_lst.append(b)
                if len(set(tmp_lst)) != len(tmp_lst):
                    return False

        return True


if __name__ == "__main__":
    print(Solution().isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
