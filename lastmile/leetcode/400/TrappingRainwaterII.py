import heapq
from typing import List


class TrappingRainwaterII:
    def trapRainWater(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        R = len(grid)
        C = len(grid[0])

        pq = []

        seen = set()
        for r in range(R):
            pq.append((grid[r][0], r, 0))
            pq.append((grid[r][C - 1], r, C - 1))
            seen.add((r, 0))
            seen.add((r, C - 1))

        for c in range(C):
            pq.append((grid[0][c], 0, c))
            pq.append((grid[R - 1][c], R - 1, c))
            seen.add((0, c))
            seen.add((R - 1, c))

        heapq.heapify(pq)

        maxHeight = float('-inf')
        result = 0
        while pq:
            height, r, c, = heapq.heappop(pq)
            maxHeight = max(maxHeight, grid[r][c])

            npairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in npairs:
                if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen:
                    if maxHeight > grid[nr][nc]:
                        result += maxHeight - grid[nr][nc]
                    heapq.heappush(pq, (grid[nr][nc], nr, nc))
                    seen.add((nr, nc))
        return result


if __name__ == '__main__':
    init = TrappingRainwaterII()
    print(init.trapRainWater([
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]))  # 4
