from typing import List


class WordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R=len(board)
        C=len(board[0])

        seen=set()
        for r in range(R):
            for c in range(C):
                if board[r][c]==word[0]:
                    if self.dfs(board, word, seen, R, C, r, c, 0):
                        return True
        return False

    def dfs(self, board, word, seen, R, C, r, c, index):
        if len(word)-1==index:
            return True

        seen.add((r,c))
        npairs=[(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        for nr, nc in npairs:
            if -1<nr<R and -1<nc<C and board[nr][nc]==word[index+1] and (nr,nc) not in seen:
                if self.dfs(board, word, seen, R, C, nr, nc, index+1):
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

    board=[["a","a"]]
    print(init.exist(board, "aaa"))  # True

    board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    print(init.exist(board, "ABCB"))  # True
