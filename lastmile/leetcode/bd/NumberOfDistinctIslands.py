from typing import List


class NumberOfDistinctIslands:
    # def numDistinctIslands(self, grid: List[List[int]]) -> int:
    #     distinctIslands = set()
    #
    #     R = len(grid)
    #     C = len(grid[0])
    #
    #     for r in range(R):
    #         for c in range(C):
    #             if grid[r][c] == 1:
    #                 currIsland = []
    #                 self.dfs(grid, R, C, r, c, currIsland, (0, 0))
    #                 distinctIslands.add(tuple(currIsland))
    #
    #     return len(distinctIslands)
    #
    # def dfs(self, grid, R, C, r, c, currIsland, pos):
    #     if -1 < r < R and -1 < c < C and grid[r][c] == 1:
    #         grid[r][c] = 0
    #         currIsland.append(pos)
    #         nei = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #         for ar, ac in nei:
    #             self.dfs(grid, R, C, r + ar, c + ac, currIsland, (pos[0]+ar, pos[1]+ac))

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        patterns = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    pattern = [(0, 0)]
                    self.dfs(grid, R, C, pattern, r, c)
                    patterns.add(tuple(pattern))

        return len(patterns)

    def dfs(self, grid, R, C, pattern, r, c):
        grid[r][c] = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if -1 < nr < R and -1 < nc < C and grid[nr][nc] == 1:
                pattern.append((dr, dc))
                self.dfs(grid, R, C, pattern, nr, nc)

if __name__ == '__main__':
    init = NumberOfDistinctIslands()
    # print(init.numDistinctIslands([[1, 1, 0, 0, 0],
    #                                [1, 1, 0, 0, 0],
    #                                [0, 0, 0, 1, 1],
    #                                [0, 0, 0, 1, 1]]
    #                               ))  # 1
    #
    # print(init.numDistinctIslands([[1, 1, 0, 1, 1],
    #                                [1, 0, 0, 0, 0],
    #                                [0, 0, 0, 0, 1],
    #                                [1, 1, 0, 1, 1]]))  # 3

    print(init.numDistinctIslands([[1, 1, 0],
                                   [0, 1, 1],
                                   [0, 0, 0],
                                   [1, 1, 1],
                                   [0, 1, 0]])) #2
