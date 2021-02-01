from collections import defaultdict
from typing import List


class SortTheMatrixDiagonally:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        matValues=defaultdict(list)
        R=len(mat)
        C=len(mat[0])
        for r in range(R):
            for c in range(C):
                matValues[r-c].append(mat[r][c])

        for key in matValues:
            matValues[key].sort(reverse=True)

        for r in range(R):
            for c in range(C):
                mat[r][c]=matValues[r-c].pop()

        return mat



if __name__ == '__main__':
    init = SortTheMatrixDiagonally()
    print(init.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])) #[[1,1,1,1],[1,2,2,2],[1,2,3,3]]

