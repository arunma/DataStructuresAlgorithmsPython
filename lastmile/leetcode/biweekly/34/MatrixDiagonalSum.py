from typing import List


class MatrixDiagonalSum:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0

        R=len(mat)
        C=len(mat[0])
        sum=0
        for r in range(R):
            for c in range(C):
                if r==c:
                    sum+=mat[r][c]

        for r in range(R):
            for c in reversed(range(C)):
                if r==R-c-1:
                    sum+=mat[r][c]

        if R%2==1:
            sum-=mat[R//2][C//2]
        return sum




if __name__ == '__main__':
    init = MatrixDiagonalSum()
    print(init.diagonalSum(mat=[[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]))  # 25
    print(init.diagonalSum(mat=[[1, 1, 1, 1],
                                [1, 1, 1, 1],
                                [1, 1, 1, 1],
                                [1, 1, 1, 1]]))  # 8
