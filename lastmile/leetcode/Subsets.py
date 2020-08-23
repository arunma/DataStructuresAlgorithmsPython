class Subsets:

    def subsetsBacktrack(self, arr):
        result=[]
        curr=[]
        arr.sort()
        self.subsetsBacktrackInner(arr, curr, result, 0)
        return result

    def subsetsBacktrackInner(self, arr, curr, result, start):
        result.append(curr.copy())
        for i in range(start, len(arr)):
            if i>start and arr[i]==arr[i-1]: continue
            curr.append(arr[i])
            self.subsetsBacktrackInner(arr, curr, result, i+1)
            curr.pop()




if __name__ == '__main__':
    init = Subsets()
    print(init.subsetsBacktrack([1, 1, 2]))

