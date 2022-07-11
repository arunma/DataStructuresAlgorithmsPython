import heapq
from typing import List


class KClosestPointsToOrigin:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i, (x, y) in enumerate(points):
            heapq.heappush(pq, (self.euclidean(x, y), x, y, i))

        result = []

        for _ in range(k):
            dist, x, y, i = heapq.heappop(pq)
            result.append([x, y])
        return result

    def euclidean(self, x, y):
        return abs(x**2 + y**2)

if __name__ == '__main__':
    init = KClosestPointsToOrigin()
    #print(init.kClosest([[1,3],[-2,2],[2,-2]], 2))
    #print(init.kClosest([[1,3],[-2,2]], 1)) #[[-2,2]]
    print(init.kClosest([[-5,4],[-6,-5],[4,6]], 2)) #[[-5,4],[4,6]]
