class MathematicalOperations:
    def calculateSumTo100(self, arr):
        result=[]
        curr=""
        sum=0
        self.helper(arr, result, curr, sum, 0)
        return result

    def helper(self, arr, result, curr, sum, index):
        if index==len(arr) and sum==100:
            result.append(curr)
            return

        for i in range(index+1, len(arr)+1):
            subs=arr[index:i]
            self.helper(arr, result, curr+'+'+subs, sum+int(subs), i)
            self.helper(arr, result, curr+'-'+subs, sum-int(subs), i)


if __name__ == '__main__':
    init = MathematicalOperations()
    print(init.calculateSumTo100("123456789"))
