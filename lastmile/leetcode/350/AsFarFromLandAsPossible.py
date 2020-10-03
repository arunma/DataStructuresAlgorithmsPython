from typing import List


class AsFarFromLandAsPossible:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = []
        R = len(grid)
        C = len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    queue.append((r, c))

        if R * C == len(queue) or len(queue) == 0:
            return -1

        level = 0
        while queue:
            lsize = len(queue)
            for i in range(lsize):
                r, c = queue.pop(0)
                npairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nr, nc in npairs:
                    if -1 < nr < R and -1 < nc < C and grid[nr][nc] == 0:
                        queue.append((nr, nc))
                        grid[nr][nc] = 1
            level += 1
        return level - 1


if __name__ == '__main__':
    init = AsFarFromLandAsPossible()
    print(init.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))  # 2
    print(init.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))  # 4
    print(init.maxDistance(
        [[1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
         [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
         [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
         [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
         [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]]))  # 2
