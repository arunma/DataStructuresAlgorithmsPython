from typing import List


class PascalsTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1] * (i + 1) for i in range(numRows)]
        for r in range(2, numRows):
            for c in range(1, r):
                tri[r][c]=tri[r-1][c-1] + tri[r-1][c]
        return tri



if __name__ == '__main__':
    init = PascalsTriangle()
    print(init.generate(numRows = 5)) #Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]))
