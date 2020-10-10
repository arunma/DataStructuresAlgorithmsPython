import sys
from typing import List


class FindTheCityWithTheSmallestNumberOfNeighboursAtAThresholdDistance:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distances = [[sys.maxsize] * n for _ in range(n)]

        for u, v, w in edges:
            distances[u][v] = w
            distances[v][u] = w

        for i in range(n):
            distances[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        counts = {}

        for i, dist in enumerate(distances):
            counts[len([d for d in dist if d <= distanceThreshold])] = i

        return counts[min(counts)]





if __name__ == '__main__':
    init = FindTheCityWithTheSmallestNumberOfNeighboursAtAThresholdDistance()
    print(init.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4)) #3
    print(init.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2)) #0

