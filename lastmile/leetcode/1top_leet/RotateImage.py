from typing import List


class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix)

        for r in range(R):
            for c in range(r, C):
                matrix[r][c], matrix[c][r]=matrix[c][r], matrix[r][c]

        for r in range(R):
            matrix[r].reverse()


if __name__ == '__main__':
    init = RotateImage()
    mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    init.rotate(mat1)
    mat2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    init.rotate(mat2)
    print(mat1)
    print(mat2)
