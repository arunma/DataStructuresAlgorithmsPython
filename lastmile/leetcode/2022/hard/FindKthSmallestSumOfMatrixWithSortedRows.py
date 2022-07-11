import heapq
from typing import List


class FindKthSmallestSumOfMatrixWithSortedRows:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        R=len(mat)
        C=len(mat[0])

        pq1=[0]

        for r in range(R):
            pq2=[]
            while pq1:
                s=heapq.heappop(pq1)
                for c in range(C):
                    heapq.heappush(pq2, -s+mat[r][c])

                while len(pq2)>k:
                    heapq.heappop(pq2)

                pq1=pq2.copy()

        return pq1[0]



if __name__ == '__main__':
    init = FindKthSmallestSumOfMatrixWithSortedRows()
    print(init.kthSmallest(mat = [[1,3,11],[2,4,6]], k=5))
