from typing import List


class SurroundedRegions:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        R = len(board)
        C = len(board[0])
        for r in range(R):
            if board[r][0] == 'O':
                self.dfs(board, r, 0)
            if board[r][C - 1] == 'O':
                self.dfs(board, r, C - 1)

        for c in range(C):
            if board[0][c] == 'O':
                self.dfs(board, 0, c)
            if board[R - 1][c] == 'O':
                self.dfs(board, R - 1, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == '*':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        return

    # def dfs(self, board, r, c):
    #     R = len(board)
    #     C = len(board[0])
    #     if r < 0 or c < 0 or r > R - 1 or c > C - 1 or board[r][c] == 'X':
    #         return
    #     else:
    #         if board[r][c] == 'O':
    #             board[r][c] = '*'
    #         if r > 1 and board[r - 1][c] == 'O':
    #             self.dfs(board, r - 1, c)
    #         if r < R - 2 and board[r + 1][c] == 'O':
    #             self.dfs(board, r + 1, c)
    #         if c > 1 and board[r][c - 1] == 'O':
    #             self.dfs(board, r, c - 1)
    #         if c < C - 2 and board[r][c + 1] == 'O':
    #             self.dfs(board, r, c + 1)
    #     return

    # def dfs(self, board, r, c):
    #     R = len(board)
    #     C = len(board[0])
    #     board[r][c] = '*'
    #     npairs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    #     for nrow, ncol in npairs:
    #         if -1 < nrow < R and -1 < ncol < C and board[nrow][ncol] == '0':
    #             self.dfs(board, nrow, ncol)

    def dfs (self, board, r,c):
        R=len(board)
        C=len(board[0])
        if -1<r<R or -1<c<C or board[r][c]=='X':
            return
        board[r][c]='*'
        npairs=[(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in npairs:
            self.dfs(board, nr, nc)

if __name__ == '__main__':
    init = SurroundedRegions()
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    init.solve(board)
    print(board)
    board = [["O", "O"], ["O", "O"]]
    init.solve(board)
    print(board)

    board = [["X", "O", "X"],
             ["O", "X", "O"],
             ["X", "O", "X"]]
    init.solve(board)
    print(board)
