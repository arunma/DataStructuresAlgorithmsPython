from typing import List


class NumberOfIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])

        num_islands = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    self.dfs(grid, R, C, r, c)
                    num_islands += 1

        return num_islands

    def dfs(self, grid, R, C, r, c):
        grid[r][c] = '0'

        neis = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        for nr, nc in neis:
            if -1 < nr < R and -1 < nc < C and grid[nr][nc] == "1":
                self.dfs(grid, R, C, nr, nc)
        return


if __name__ == "__main__":
    init = NumberOfIslands()
    print(init.numIslands(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))
