class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.antidiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        tot = 1 if player == 1 else -1
        self.rows[row] += tot
        self.cols[col] += tot
        if row == col:
            self.diag += tot
        if row == self.n - col - 1:
            self.antidiag += tot

        if abs(self.diag) == self.n or abs(self.antidiag) == self.n or abs(self.rows[row])==self.n or abs(self.cols[col])==self.n:
            return player
        return 0


if __name__ == '__main__':
    toe = TicTacToe(3)
    print(toe.move(0, 0, 1))  # -> Returns 0 (no one wins)
    '''
    |X| | |
    | | | |    // Player 1 makes a move at (0, 0).
    | | | |
    '''

    print(toe.move(0, 2, 2))  # -> Returns 0 (no one wins)
    '''
    |X| |O|
    | | | |    // Player 2 makes a move at (0, 2).
    | | | |
    '''

    print(toe.move(2, 2, 1))  # -> Returns 0 (no one wins)
    '''
    |X| |O|
    | | | |    // Player 1 makes a move at (2, 2).
    | | |X|
    '''

    print(toe.move(1, 1, 2))  # -> Returns 0 (no one wins)
    '''
    |X| |O|
    | |O| |    // Player 2 makes a move at (1, 1).
    | | |X|
    '''

    print(toe.move(2, 0, 1))  # -> Returns 0 (no one wins)
    '''
    |X| |O|
    | |O| |    // Player 1 makes a move at (2, 0).
    |X| |X|
    '''

    print(toe.move(1, 0, 2))  # -> Returns 0 (no one wins)
    '''
    |X| |O|
    |O|O| |    // Player 2 makes a move at (1, 0).
    |X| |X|
    '''

    print(toe.move(2, 1, 1))  # -> Returns 1 (player 1 wins)
    '''
    |X| |O|
    |O|O| |    // Player 1 makes a move at (2, 1).
    |X|X|X|
    '''
