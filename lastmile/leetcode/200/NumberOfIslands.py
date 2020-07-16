from typing import List





class NumberOfIslands:
    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return
        else:
            grid[r][c] = '0'
            self.dfs(grid, r - 1, c)
            self.dfs(grid, r + 1, c)
            self.dfs(grid, r, c - 1)
            self.dfs(grid, r, c + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        R = len(grid)
        C = len(grid[0])
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    count += 1
        return count


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
