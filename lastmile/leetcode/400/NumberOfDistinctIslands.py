from typing import List


class NumberOfDistinctIslands:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        R = len(grid)
        C = len(grid[0])

        distIslands = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    currIsland = []
                    self.dfs(grid, r, c, R, C, currIsland, (0, 0))
                    distIslands.add(tuple(currIsland))

        return len(distIslands)

    def dfs(self, grid, r, c, R, C, currIsland, pos):
        if -1 < r < R and -1 < c < C and grid[r][c] == 1:
            grid[r][c] = 0
            currIsland.append(pos)
            neis = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for nr, nc in neis:
                self.dfs(grid, r + nr, c + nc, R, C, currIsland, (pos[0] + nr, pos[1] + nc))


if __name__ == '__main__':
    init = NumberOfDistinctIslands()
    # print(init.numDistinctIslands([[1, 1, 0, 0, 0],
    #                                [1, 1, 0, 0, 0],
    #                                [0, 0, 0, 1, 1],
    #                                [0, 0, 0, 1, 1]]
    #                               ))
    #
    # print(init.numDistinctIslands([[1, 1, 0],
    #                                [0, 1, 1],
    #                                [0, 0, 0],
    #                                [1, 1, 1],
    #                                [0, 1, 0]]))

    print(init.numDistinctIslands([[1, 1, 0, 1, 1],
                                   [1, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 1],
                                   [1, 1, 0, 1, 1]]))
