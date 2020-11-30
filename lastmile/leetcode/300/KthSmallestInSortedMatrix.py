import heapq
from typing import List


class KthSmallestInSortedMatrix:
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     R = len(matrix)
    #     C = len(matrix[0])
    #     pq=[]
    #     for r in range(R):
    #         for c in range(C):
    #             heapq.heappush(pq, -matrix[r][c])
    #             if len(pq)>k:
    #                 heapq.heappop(pq)
    #     return -pq[0]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []

        for r in range(len(matrix)):
            heapq.heappush(pq, (matrix[r][0], r, 0))

        numCounter = 0
        number = 0

        while pq:
            value, row, col = heapq.heappop(pq)
            numCounter += 1

            if numCounter == k:
                return value

            if col < len(matrix[0]) - 1:
                heapq.heappush(pq, (matrix[row][col + 1], row, col + 1))

        return -1


if __name__ == '__main__':
    init = KthSmallestInSortedMatrix()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    print(init.kthSmallest(matrix, 8))  # 13
