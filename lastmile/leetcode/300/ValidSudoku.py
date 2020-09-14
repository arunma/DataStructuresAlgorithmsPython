from typing import List


class ValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False

        return self.isRowsValid(board) and self.isColsValid(board) and self.isBlocksValid(board)

    def isRowsValid(self, board):
        for r in board:
            if not self.isArrayValid(r):
                return False
        return True

    def isColsValid(self, board):
        for c in list(zip(*board)):
            if not self.isArrayValid(c):
                return False
        return True

    def isBlocksValid(self, board):
        R = len(board)
        C = len(board[0])

        for r in range(0, R, 3):
            for c in range(0, C, 3):
                minboard = [board[x][y] for x in range(r, r + 3) for y in range(c, c + 3)]
                if not self.isArrayValid(minboard):
                    return False
        return True

    def isArrayValid(self, arr):
        seen = set()
        for num in arr:
            if num != '.' and num in seen:
                return False
            seen.add(num)
        return True


if __name__ == '__main__':
    init = ValidSudoku()
    sudoku1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(init.isValidSudoku(sudoku1))  # True
    sudoku2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    print(init.isValidSudoku(sudoku2))  # False

    sudoku3 = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
               [".", "4", ".", "3", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", "3", ".", ".", "1"],
               ["8", ".", ".", ".", ".", ".", ".", "2", "."],
               [".", ".", "2", ".", "7", ".", ".", ".", "."],
               [".", "1", "5", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", "2", ".", ".", "."],
               [".", "2", ".", "9", ".", ".", ".", ".", "."],
               [".", ".", "4", ".", ".", ".", ".", ".", "."]]
    print(init.isValidSudoku(sudoku3))  # False
