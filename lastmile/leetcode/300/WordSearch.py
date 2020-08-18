from typing import List


class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        visited = [[False] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if self.search(board, r, c, word, visited, 0):
                        return True
        return False

    def search(self, board, r, c, word, visited, index):
        if index == len(word) - 1:
            return True

        visited[r][c] = True
        if r > 0 and not visited[r - 1][c] and board[r - 1][c] == word[index + 1] \
                and self.search(board, r - 1, c, word, visited, index + 1):
            return True
        if c > 0 and not visited[r][c - 1] and board[r][c - 1] == word[index + 1] \
                and self.search(board, r, c - 1, word, visited, index + 1):
            return True
        if r < len(board) - 1 and not visited[r + 1][c] and board[r + 1][c] == word[index + 1] \
                and self.search(board, r + 1, c, word, visited, index + 1):
            return True
        if c < len(board[0]) - 1 and not visited[r][c + 1] and board[r][c + 1] == word[index + 1] \
                and self.search(board, r, c + 1, word, visited, index + 1):
            return True

        visited[r][c] = False
        return False


if __name__ == '__main__':
    init = WordSearch()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(init.exist(board, "ABCCED"))  # True
    print(init.exist(board, "SEE"))  # True
    print(init.exist(board, "ABCB"))  # True
