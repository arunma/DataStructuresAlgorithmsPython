import heapq
from typing import List


class KClosestToOrigin:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not k:
            return []

        pq = []
        for x, y in points:
            heapq.heappush(pq, (self.euc_distance(x, y), x, y))

        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(pq)
            result.append([x, y])

        return result

    def euc_distance(self, x, y):
        return x**2 + y**2  # Since it's distance from origin anyway


if __name__ == "__main__":
    init = KClosestToOrigin()
    #print(init.kClosest(points=[[1, 3], [-2, 2]], k=1))  # [[-2,2]]
    #print(init.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))  # [[3,3],[-2,4]]
    print(init.kClosest(points=[[-5, 4], [-6, -5], [4, 6]], k=2))  # [[-5,4],[4,6]]
