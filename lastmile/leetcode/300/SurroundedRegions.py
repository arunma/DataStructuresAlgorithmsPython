from typing import List


class SurroundedRegions:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board
        R = len(board)
        C = len(board[0])
        for r in range(R):
            if board[r][0] == 'O':
                self.dfs(board, R, C, r, 0)
            if board[r][C - 1] == 'O':
                self.dfs(board, R, C, r, C - 1)

        for c in range(C):
            if board[0][c] == 'O':
                self.dfs(board, R, C, 0, c)
            if board[R - 1][c] == 'O':
                self.dfs(board, R, C, R - 1, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '*':
                    board[r][c] = 'O'
        return board

    # def dfs(self, board, R, C, r, c):
    #     if r < 0 or c < 0 or r == R or c == C or board[r][c] == 'X' or board[r][c]=='*':
    #         return
    #     if board[r][c] == 'O':
    #         board[r][c] = '*'
    #     neigbours = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    #     for ro, co in neigbours:
    #         self.dfs(board, R, C, r + ro, c + co)

    def dfs(self, board, R, C, r, c):
        board[r][c] = '*'
        npairs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nrow, ncol in npairs:
            if -1 < nrow < R and -1 < ncol < C and board[nrow][ncol]=='0':
                self.dfs(board, R, C, nrow, ncol)


if __name__ == '__main__':
    init = SurroundedRegions()
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    print(init.solve(board))
    '''
    X X X X
    X X X X
    X X X X
    X O X X
    '''

    board = [["X", "O", "X"],
             ["O", "X", "O"],
             ["X", "O", "X"]]
    '''
    [['X', 'O', 'X'], 
    ['O', 'X', 'O'], 
    ['X', 'O', 'X']]
    '''

    print(init.solve(board))

    board = [["O", "O"], ["O", "O"]]
    print(init.solve(board))
