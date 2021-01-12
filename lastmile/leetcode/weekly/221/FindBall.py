from typing import List


class FindBall:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R=len(grid)
        C=len(grid[0])
        result=[0]* C

        for i in range(C):
            start=i
            state=1
            for j in range(0, R):
                if grid[j][start]==1:
                    if start>=C-1 or grid[j][start+1]==-1:
                        state=-1
                        break
                    start+=1
                else:
                    if start<=0 or grid[j][start-1]==1:
                        state=-1
                        break
                    start-=1
            if state==-1:
                result[i]= state
            else:
                result[i]=start
        return result




if __name__ == '__main__':
    init = FindBall()
    print(init.findBall(grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
    print(init.findBall(grid = [[-1]]))
    print(init.findBall(grid = [[1]]))

