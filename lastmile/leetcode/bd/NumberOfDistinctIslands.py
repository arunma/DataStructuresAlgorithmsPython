from typing import List


class NumberOfDistinctIslands:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinctIslands = set()

        R = len(grid)
        C = len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    currIsland = []
                    self.dfs(grid, R, C, r, c, currIsland, (0, 0))
                    distinctIslands.add(tuple(currIsland))

        return len(distinctIslands)

    def dfs(self, grid, R, C, r, c, currIsland, pos):
        if -1 < r < R and -1 < c < C and grid[r][c] == 1:
            grid[r][c] = 0
            currIsland.append(pos)
            nei = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for ar, ac in nei:
                self.dfs(grid, R, C, r + ar, c + ac, currIsland, (pos[0]+ar, pos[1]+ac))


if __name__ == '__main__':
    init = NumberOfDistinctIslands()
    print(init.numDistinctIslands([[1, 1, 0, 0, 0],
                                   [1, 1, 0, 0, 0],
                                   [0, 0, 0, 1, 1],
                                   [0, 0, 0, 1, 1]]
                                  ))  # 1

    print(init.numDistinctIslands([[1, 1, 0, 1, 1],
                                   [1, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 1],
                                   [1, 1, 0, 1, 1]]))  # 3

    # print(init.numDistinctIslands([[1, 1, 0],
    #                                [0, 1, 1],
    #                                [0, 0, 0],
    #                                [1, 1, 1],
    #                                [0, 1, 0]]))
