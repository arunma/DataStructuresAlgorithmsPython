class MultiplyTwoArbitraryPrecisionIntegers:
    def multiply(self, A, B):

        sign = -1 if A[0] ^ B[0] else 1
        A[0]=abs(A[0])
        B[0]=abs(B[0])

        result=[0]* (len(A)+len(B))

        for i in reversed(range(len(A))):
            for j in reversed(range(len(B))):
                result[i+j+1]+=A[i]*B[j]
                result[i+j]+=result[i+j+1]//10
                result[i+j+1]%=10

        start=0
        for i, num in enumerate(result):
            if num==0:
                start=i+1

        result=result[start:]
        result[0]=result[0]*sign

        return result




if __name__ == '__main__':
    init = MultiplyTwoArbitraryPrecisionIntegers()
    print(init.multiply([1, 2], [1, 1]))
    print(init.multiply([1, 9, 3, 7, 0, 7, 7, 2, 1],
                        [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]))  # -1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7
