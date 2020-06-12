from typing import List
from math import sqrt, pow
import heapq


class KClosest:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # distance = [(sqrt(pow(point[0], 2) + pow(point[1], 2)), point) for point in points]
        # return [point for dist, point in sorted(distance)[:K]]
        # return heapq.nsmallest(K, points, lambda p: p[0]*p[0] + p[1]*p[1])
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:K]


if __name__ == '__main__':
    init = KClosest()
    print(init.kClosest([[1, 3], [-2, 2]], 1))  # -2,2
    print(init.kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2))  # [[3,3],[-2,4]]
