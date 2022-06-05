from typing import List


class SpiralMatrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R=len(matrix)
        C=len(matrix[0])

        rb=0
        re=R-1
        cb=0
        ce=C-1

        result=[]
        while rb<=re and cb<=ce:
            for i in range(cb, ce+1):
                result.append(matrix[rb][i])
            rb+=1


            for i in range(rb, re+1):
                result.append(matrix[i][ce])
            ce-=1

            if rb<=re:
                for i in reversed(range(cb, ce+1)):
                    result.append(matrix[re][i])
                re-=1

            if cb <= ce:
                for i in reversed(range(rb, re+1)):
                    result.append(matrix[i][cb])
                cb+=1

        print(result)


if __name__ == '__main__':
    init = SpiralMatrix()
    #init.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    init.spiralOrder(matrix = [[1,2,3,4],[10,11,12,5],[9,8,7,6]])