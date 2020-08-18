import heapq
from typing import List


class KthSmallestInSortedMatrix:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        R = len(matrix)
        C = len(matrix[0])
        pq=[]
        for r in range(R):
            for c in range(C):
                heapq.heappush(pq, -matrix[r][c])
                if len(pq)>k:
                    heapq.heappop(pq)
        return -pq[0]


if __name__ == '__main__':
    init = KthSmallestInSortedMatrix()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    print(init.kthSmallest(matrix, 8))  # 13
