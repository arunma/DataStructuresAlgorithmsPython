from typing import List


class WordSearch:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     R = len(board)
    #     C = len(board[0])
    #
    #     visited = [[False] * C for _ in range(R)]
    #     for r in range(R):
    #         for c in range(C):
    #             if board[r][c] == word[0]:
    #                 if self.search(board, r, c, word, visited, 0):
    #                     return True
    #     return False
    #
    # def search(self, board, r, c, word, visited, index):
    #     if index == len(word) - 1:
    #         return True
    #
    #     visited[r][c] = True
    #
    #     if r > 0 and not visited[r - 1][c] and board[r - 1][c] == word[index + 1] \
    #             and self.search(board, r - 1, c, word, visited, index + 1):
    #         return True
    #     if c > 0 and not visited[r][c - 1] and board[r][c - 1] == word[index + 1] \
    #             and self.search(board, r, c - 1, word, visited, index + 1):
    #         return True
    #     if r < len(board) - 1 and not visited[r + 1][c] and board[r + 1][c] == word[index + 1] \
    #             and self.search(board, r + 1, c, word, visited, index + 1):
    #         return True
    #     if c < len(board[0]) - 1 and not visited[r][c + 1] and board[r][c + 1] == word[index + 1] \
    #             and self.search(board, r, c + 1, word, visited, index + 1):
    #         return True
    #
    #     visited[r][c] = False
    #     return False

    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     R = len(board)
    #     C = len(board[0])
    #
    #     visited = [[False] * C for _ in range(R)]
    #     for r in range(R):
    #         for c in range(C):
    #             if board[r][c] == word[0]:
    #                 if (self.dfs(board, word, visited, r, c)):
    #                     return True
    #
    #     return False
    #
    # def dfs(self, board, word, visited, r, c):
    #     if not word:
    #         return True
    #     visited[r][c] = True
    #     npairs = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
    #     for nrow, ncol in npairs:
    #         if -1 < nrow < len(board) and -1 < ncol < len(board[0]) and board[r][c] == word[0] and not visited[nrow][ncol]:
    #             if self.dfs(board, word[1:], visited, nrow, ncol):
    #                 return True
    #     visited[r][c] = False
    #     return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        visited = [[False] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0] and not visited[r][c]:
                    if self.search(board, r, c, word, visited, 0):
                        return True
        return False

    def search(self, board, r, c, word, visited, index):
        if index == len(word) - 1:
            return True

        visited[r][c] = True

        npairs = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]
        for nrow, ncol in npairs:
            if -1<nrow<len(board) and -1<ncol<len(board[0]) and not visited[nrow][ncol] and board[nrow][ncol]==word[index+1] and self.search(board, nrow, ncol,word, visited, index+1):
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
    print(init.exist(board, "ABCB"))  # False

    board = [['a']]
    print(init.exist(board, "a"))  # True
