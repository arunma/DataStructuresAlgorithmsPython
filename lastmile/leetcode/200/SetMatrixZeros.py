from typing import List

class MatrixZeros:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rz = set()
        cz = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rz.add(r)
                    cz.add(c)

        for r in range(len(matrix)):
            if r in rz:
                for c in range(len(matrix[0])):
                    matrix[r][c]=0

        for c in range(len(matrix[0])):
            if c in cz:
                for r in range(len(matrix)):
                    matrix[r][c]=0



if __name__ == '__main__':
    init=MatrixZeros()
    print(init.setZeroes([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])) #[[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(init.setZeroes([
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]))#[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
