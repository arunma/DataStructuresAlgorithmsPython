from typing import List


class NumberOfIslands:
    # def numIslands(self, grid):
    #     if not grid:
    #         return 0
    #     R = len(grid)
    #     C = len(grid[0])
    #
    #     islands = 0
    #     for r in range(R):
    #         for c in range(C):
    #             if grid[r][c] == '1':
    #                 self.dfs(r, c, R, C, grid)
    #                 islands += 1
    #
    #     return islands
    #
    # def dfs(self, r, c, R, C, grid):
    #     if -1<r<R and -1<c<C and grid[r][c] == '1':
    #         grid[r][c] = '0'
    #         self.dfs(r + 1, c, R, C, grid)
    #         self.dfs(r - 1, c, R, C, grid)
    #         self.dfs(r, c + 1, R, C, grid)
    #         self.dfs(r, c - 1, R, C, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        R = len(grid)
        C = len(grid[0])

        islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    self.dfs(grid, R, C, r, c)
                    islands += 1

        return islands

    def dfs(self, grid, R, C, r, c):

        if not -1 < r < R or not -1 < c < C or grid[r][c] == '0':
            return

        grid[r][c] = '0'
        npairs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in npairs:
            self.dfs(grid, R, C, nr, nc)


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


