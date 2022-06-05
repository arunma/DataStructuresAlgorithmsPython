from typing import List


class SetMatrixZeros:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])

        cand_r = set()
        cand_c = set()

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    cand_r.add(r)
                    cand_c.add(c)

        for r in range(R):
            for c in range(C):
                if r in cand_r or c in cand_c:
                    matrix[r][c] = 0
        return matrix


if __name__ == '__main__':
    init=SetMatrixZeros()
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
