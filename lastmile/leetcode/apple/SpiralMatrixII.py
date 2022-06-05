from typing import List


class SpiralMatrixII:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]* n for _ in range(n)]
        rb=0
        re=n-1
        cb=0
        ce=n-1

        val=1
        while rb<=re and cb<=ce:
            #Left to right
            for i in range(cb, ce+1):
                matrix[rb][i]=val
                val+=1
            rb+=1

            #Top to bottom
            for i in range(rb, re + 1):
                matrix[i][ce] = val
                val += 1
            ce-=1

            #Right to Left
            for i in reversed(range(cb, ce+1)):
                matrix[re][i]=val
                val+=1
            re-=1

            #Bottom to top
            for i in reversed(range(rb, re+1)):
                matrix[i][cb]=val
                val+=1
            cb+=1

        return matrix



if __name__ == '__main__':
    init = SpiralMatrixII()
    print(init.generateMatrix(3)) #[[1,2,3],[8,9,4],[7,6,5]]
