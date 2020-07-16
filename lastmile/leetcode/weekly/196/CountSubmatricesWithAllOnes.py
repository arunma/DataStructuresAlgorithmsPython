from typing import List

# DOES NOT WORK
class CountSubmatricesWithAllOnes:
    def numSubmat(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])
        # dp = [[0] * (C) for _ in range(R)]

        count = 0
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 1 and r > 0 and c > 0:
                    mat[r][c] = min(mat[r - 1][c] , mat[r][c - 1]) + 1
                    count += mat[r][c]

        return count


if __name__ == '__main__':
    init = CountSubmatricesWithAllOnes()
    print(init.numSubmat(mat=[[1, 0, 1],
                              [1, 1, 0],
                              [1, 1, 0]]))  # 13

    print(init.numSubmat(mat=[[0, 1, 1, 0],
                              [0, 1, 1, 1],
                              [1, 1, 1, 0]]))  # 24
