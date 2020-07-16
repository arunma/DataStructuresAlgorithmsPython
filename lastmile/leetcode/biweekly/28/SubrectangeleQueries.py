from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.grid = rectangle
        self.R = len(rectangle)
        self.C = len(rectangle[0])

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        if row1<0 or row1>self.R-1 or row2<0 or row2>self.R-1 or col1<0 or col1>self.C-1 or col2<0 or col2>self.C-1:
            return
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.grid[r][c] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.grid[row][col]

if __name__ == '__main__':
    init = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
    print(init.getValue(0,2))#1
    init.updateSubrectangle(0,0,3,2,5)
    print(init.getValue(0,2))#5
    print(init.getValue(3,1))#5
    init.updateSubrectangle(3,0,3,2,10)
    print(init.getValue(3,1)) #10
    print(init.getValue(0,2)) #5
