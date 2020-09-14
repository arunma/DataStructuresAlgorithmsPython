class MinimumNumberOfOperationsFor1:
    def minOperations(self, input):
        if input==0 or input==1:
            return 0
        if input%2==0:
            return 1 + self.minOperations(input//2)

        add=1+ self.minOperations(input+1)
        sub=1+ self.minOperations(input-1)
        return min(add, sub)



if __name__ == '__main__':
    init = MinimumNumberOfOperationsFor1()
    print(init.minOperations(15)) #5
