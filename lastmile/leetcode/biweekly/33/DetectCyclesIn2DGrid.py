from collections import defaultdict
from itertools import count
from typing import List


class DetectCyclesIn2DGrid:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        R = len(grid)
        C = len(grid[0])

        def hasCycle(grid, r, c, color, pr, pc, val):
            color[r, c] = GRAY
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc]==val and (nr!=pr or nc!=pc):
                    if color[nr, nc] == GRAY:
                        return True
                    if color[nr,nc]==WHITE:
                        if hasCycle(grid, nr, nc, color, r,c, val):
                            return True
            color[r, c] = BLACK
            return False

        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if color[r, c] == WHITE:
                    if hasCycle(grid, r, c, color, -1, -1, val):
                        return True

        return False


if __name__ == '__main__':
    init = DetectCyclesIn2DGrid()
    print(init.containsCycle(
        grid=[["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]))  # true
    print(init.containsCycle(grid=[["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]))  # false
    print(init.containsCycle(grid=[["a", "a", "b"]]))  # false
    print(init.containsCycle(grid=[["b", "b"]]))  # false
    print(init.containsCycle(
        grid=[["e", "d", "d", "d"], ["b", "a", "a", "b"], ["e", "b", "e", "a"], ["c", "e", "a", "d"]]))  # false
