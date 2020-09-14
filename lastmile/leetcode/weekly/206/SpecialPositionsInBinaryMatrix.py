from typing import List


class SpecialPositionsInBinaryMatrix:
    def numSpecial(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        R = len(mat)
        C = len(mat[0])

        uniq =0
        for r in range(R):
            for c in range(C):
                if mat[r][c]==1 and r==c:
                    uniq+=1

        for r in range(R):
            for c in reversed(range(C)):
                if mat[r][c] == 1 and r == c:
                    uniq += 1


        return uniq


if __name__ == '__main__':
    init = SpecialPositionsInBinaryMatrix()
    print(init.numSpecial(mat=[[1, 0, 0],
                               [0, 0, 1],
                               [1, 0, 0]])) #3

    print(init.numSpecial(mat=[[1, 0, 0],
                               [0, 1, 0],
                               [0, 0, 1]])) #3

    print(init.numSpecial(mat=[[0, 0, 1, 0],
                               [0, 0, 0, 0],
                               [0, 0, 0, 0],
                               [0, 1, 0, 0]])) #2

    print(init.numSpecial(mat=[[1, 0, 0],
                               [0, 0, 1],
                               [1, 0, 0]])) #3
