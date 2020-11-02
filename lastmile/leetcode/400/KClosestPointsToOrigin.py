import heapq
from typing import List


class KClosestPointsToOrigin:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        maxheap=[] #Min heap ideally but we want to pop the minimum

        for x,y in points:
            dist=-(x*x + y*y)
            if len(maxheap)==K:
                heapq.heappushpop(maxheap,(dist, x,y))
            else:
                heapq.heappush(maxheap, (dist, x, y))

        return [[x,y] for dist, x,y in maxheap]



if __name__ == '__main__':
    init = KClosestPointsToOrigin()
    print(init.kClosest(points = [[1,3],[-2,2]], K = 1)) #[-2,2]