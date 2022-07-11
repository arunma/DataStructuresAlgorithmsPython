from typing import List


class XMatrix:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        R=len(grid)
        C=len(grid[0])

        for r in range(R):
            for c in range(C):
                if r==c or (r+c)==R-1:
                    if grid[r][c]==0:
                        return False
                elif grid[r][c]!=0:
                    return False
        return True




if __name__ == '__main__':
    init = XMatrix()
    print(init.checkXMatrix(grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]])) #true
    print(init.checkXMatrix(grid = [[5,7,0],[0,3,1],[0,5,0]])) #false
    print(init.checkXMatrix(grid = [[0,0,0,0,1],[0,4,0,1,0],[0,0,5,0,0],[0,5,0,2,0],[4,0,0,0,2]])) #false
