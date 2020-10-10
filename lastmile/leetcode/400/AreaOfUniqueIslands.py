from typing import List


class AreaOfUniqueIslands:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        uniqueIslands = set()
        for r in range(R):
            for c in range(C):
                currIsland = []
                if grid[r][c] == 1:
                    self.dfs(grid, R, C, r, c, currIsland, (0, 0))
                    uniqueIslands.add(tuple(currIsland))

        # return len(uniqueIslands)
        area = 0
        for i in uniqueIslands:
            area += len(i)
        return area

    def dfs(self, grid, R, C, r, c, currIsland, pos):
        if -1 < r < R and -1 < c < C and grid[r][c] == 1:
            grid[r][c] = 0
            currIsland.append(pos)
            npairs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for nr, nc in npairs:
                self.dfs(grid, R, C, nr + r, nc + c, currIsland, (nr, nc))


if __name__ == '__main__':
    init = AreaOfUniqueIslands()
    print(init.numDistinctIslands([[1, 1, 0, 0, 0],
                                   [1, 1, 0, 0, 0],
                                   [0, 0, 0, 1, 1],
                                   [0, 0, 0, 1, 1]]))  # 1/4
    print(init.numDistinctIslands([[1, 1, 0, 1, 1],
                                   [1, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 1],
                                   [1, 1, 0, 1, 1]])) #3/8
