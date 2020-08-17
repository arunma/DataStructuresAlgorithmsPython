from typing import List


class ValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.is_row_valid(board) and self.is_column_valid(board) and self.is_square_valid(board)

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_column_valid(self, board):
        for col in list(zip(*board)):
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for r in (0, 3, 6):
            for c in (0, 3, 6):
                minboard = [board[x][y] for x in range(r, r + 3) for y in range(c, c + 3)]
                if not self.is_unit_valid(minboard):
                    return False
        return True

    def is_unit_valid(self, lst):
        unit = [x for x in lst if x != '.']
        return len(set(unit)) == len(unit)


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
