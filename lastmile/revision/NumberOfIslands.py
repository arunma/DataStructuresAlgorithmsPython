from typing import List


class NumberOfIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])

        num_islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c, R, C)
                    num_islands += 1
        return num_islands

    def dfs(self, grid, r, c, R, C):
        grid[r][c] = '0'

        npairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        for nr, nc in npairs:
            if -1 < nr < R and -1 < nc < C and grid[nr][nc] == '1':
                self.dfs(grid, nr, nc, R, C)


if __name__ == '__main__':
    init = NumberOfIslands()
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    print(init.numIslands(grid))  # 1

    grid2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    print(init.numIslands(grid2))  # 3
    print(init.numIslands([]))  # 0
