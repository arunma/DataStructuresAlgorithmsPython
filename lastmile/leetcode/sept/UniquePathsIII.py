from typing import List


class UniquePathsIII:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        zeros = 0
        start = (0, 0)
        target = (0, 0)
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    start = (r, c)
                elif grid[r][c] == 2:
                    target = (r, c)
                elif grid[r][c] == 0:
                    zeros += 1

        curr = []

        self.result = 0
        self.backtrack(grid, R, C, zeros, target, start[0], start[1], curr)
        return self.result

    def backtrack(self, grid, R, C, zeros, target, r, c, curr):

        if len(curr) == zeros + 1 and (r, c) == target:
            self.result += 1
            return
        oldval = grid[r][c]
        grid[r][c] = -1

        npairs = [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
        for nr, nc in npairs:
            if -1 < nr < R and -1 < nc < C and grid[nr][nc] != -1:
                self.backtrack(grid, R, C, zeros, target, nr, nc, curr + [(nr, nc)])
        grid[r][c] = oldval


if __name__ == '__main__':
    init = UniquePathsIII()
    print(init.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))  # 2
    print(init.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))  # 4
    print(init.uniquePathsIII([[0, 1], [2, 0]]))  # 0
