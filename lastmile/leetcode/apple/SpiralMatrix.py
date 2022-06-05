class SpiralMatrix:

    def spiralOrder(self, matrix):
        R=len(matrix)
        C=len(matrix[0])

        rb=0
        cb=0
        re=R-1
        ce=C-1

        result=[]

        while rb<=re and cb<=ce:
            #Left to right
            for i in range(cb, ce+1):
                result.append(matrix[rb][i])

            rb+=1

            #top to bottom
            for i in range(rb, re+1):
                result.append(matrix[i][ce])

            ce-=1

            #Right to left
            if rb<=re:
                for i in reversed(range(cb, ce+1)):
                    result.append(matrix[re][i])

                re-=1

            #Bottom to top
            if cb<ce:
                for i in reversed(range(rb, re+1)):
                    result.append(matrix[i][cb])

                cb+=1

        return result






if __name__ == '__main__':
    init = SpiralMatrix()
    #init.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    print(init.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    #init.spiralOrder(matrix=[[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]])
