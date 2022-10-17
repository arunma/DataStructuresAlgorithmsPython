from typing import List


class RottingOranges:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R=len(grid)
        C=len(grid[0])
        queue=[]
        for r in range(R):
            for c in range(C):
                if grid[r][c]==2:
                    queue.append((r,c,0))

        count=0
        while queue:
            r,c, cnt=queue.pop(0)
            count=cnt
            neis =[(r+1,c), (r-1,c), (r,c+1), (r,c-1)]
            for nr, nc in neis:
                if -1<nr<R and -1<nc<C and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    queue.append((nr,nc, cnt+1))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return -1
        return count



if __name__ == "__main__":
    init = RottingOranges()
    print(init.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) #4
    print(init.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) #-1
    print(init.orangesRotting([[0,2]])) #0
