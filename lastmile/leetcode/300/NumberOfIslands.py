class NumberOfIslands:
    def numIslands(self, grid):
        if not grid:
            return 0
        R = len(grid)
        C = len(grid[0])

        islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    self.dfs(r, c, R, C, grid)
                    islands += 1

        return islands

    def dfs(self, r, c, R, C, grid):
        if r < 0 or c < 0 or r > R - 1 or c > C - 1 or grid[r][c] == '0':
            return
        else:
            grid[r][c] = '0'
            self.dfs(r + 1, c, R, C, grid)
            self.dfs(r - 1, c, R, C, grid)
            self.dfs(r, c + 1, R, C, grid)
            self.dfs(r, c - 1, R, C, grid)


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
    print(init.numIslands([]))  # 3
