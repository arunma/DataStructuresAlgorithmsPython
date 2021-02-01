import heapq
import sys
from typing import List


class PathWithMinimumEffort:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])
        distances = [[sys.maxsize] * C for _ in range(R)]
        distances[0][0] = 0

        pq = [(0, 0, 0)]
        seen = set()

        while pq:
            dist, r, c = heapq.heappop(pq)
            seen.add((r, c))

            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in nei:
                if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen:
                    nei_distance = max(abs(heights[nr][nc] - heights[r][c]), dist)
                    if nei_distance < distances[nr][nc]:
                        distances[nr][nc] = nei_distance
                        heapq.heappush(pq, (nei_distance, nr, nc))
        return distances[-1][-1]


if __name__ == '__main__':
    init = PathWithMinimumEffort()
    print(init.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))  # 2
    print(init.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))  # 1
    print(init.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))  # 2
    print(init.minimumEffortPath(
        [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))  # 0
