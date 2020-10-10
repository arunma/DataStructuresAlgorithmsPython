from typing import List


class MaximumAreaOfIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        R = len(grid)
        C = len(grid[0])

        maxmm = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    maxmm = max(maxmm, self.dfs(grid, R, C, r, c))

        return maxmm

    def dfs(self, grid, R, C, r, c):
        if -1 < r < R and -1 < c < C and grid[r][c] == 1:
            grid[r][c] = 0
            count = 1
            npairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in npairs:
                count+= self.dfs(grid, R, C, nr, nc)
            return count
        return 0

if __name__ == '__main__':
    init = MaximumAreaOfIsland()
    print(init.maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
    print(init.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
