class PlusOne:
    def plusOne(self, A):
        A[-1]+=1

        for i in reversed(range(1, len(A))):
            if A[i]<10:
                break
            A[i]=0
            A[i-1]+=1

        if A[0]==10:
            A[0]=1
            A.append(0)

        return A




if __name__ == '__main__':
    init = PlusOne()
    print(init.plusOne([1,2,9]))
    print(init.plusOne([1,3,0]))
    print(init.plusOne([9,9,9]))
