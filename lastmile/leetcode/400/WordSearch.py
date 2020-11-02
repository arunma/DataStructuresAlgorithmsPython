from typing import List


class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        R = len(board)
        C = len(board[0])

        seen = []
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if self.dfs(board, seen, word, R, C, r, c, 0):
                        print(seen)
                        return True

        return False

    def dfs(self, board, seen, word, R, C, r, c, index):
        if len(word) - 1 == index:
            return True

        seen.append((r, c))
        npairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for nr, nc in npairs:
            if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen and board[nr][nc] == word[index + 1] and self.dfs(
                    board, seen, word, R, C, nr, nc, index + 1):
                return True
        seen.remove((r,c))
        return False



if __name__ == '__main__':
    init = WordSearch()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'E', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(init.exist(board, "ABCESEEEFS"))  # True
