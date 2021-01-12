from typing import List


class TwoSum:
    def twoSum(self, arr, target):
        small=0
        big=len(arr)-1
        while small<big:
            curr=arr[small]+arr[big]
            if curr==target:
                return [arr[small], arr[big]]
            elif curr<target:
                small+=1
            else:
                big-=1
        return [-1,-1]




if __name__ == '__main__':
    init = TwoSum()
    print(init.twoSum([1, 2, 3, 5, 6, 7], 11))
