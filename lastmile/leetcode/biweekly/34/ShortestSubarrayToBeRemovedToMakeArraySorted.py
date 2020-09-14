import sys
from typing import List


class ShortestSubarrayToBeRemovedToMakeArraySorted:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N=len(arr)
        left=0
        while left<N-1 and arr[left]<arr[left+1]:
            left+=1

        if left+1==N:
            return 0

        right=N-1
        while right>=0 and arr[right]>arr[right-1]:
            right-=1

        ans=max(left+1, N-right)

        for i in range(0, left+1):
            j = right
            while j<N and arr[j]<arr[i]:
                j+=1
            if j==N: break
            ans=max(ans, i+1+N-j)

        return N-ans







if __name__ == '__main__':
    init = ShortestSubarrayToBeRemovedToMakeArraySorted()
    print(init.findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))  # 3
    print(init.findLengthOfShortestSubarray([5, 4, 3, 2, 1]))  # 4
    print(init.findLengthOfShortestSubarray([1, 2, 3]))  # 0
    print(init.findLengthOfShortestSubarray([1]))  # 0
    print(init.findLengthOfShortestSubarray([13,0,14,7,18,18,18,16,8,15,20]))  # 8
    print(init.findLengthOfShortestSubarray([16,10,0,3,22,1,14,7,1,12,15]))  # 8
    print(init.findLengthOfShortestSubarray([2,2,2,1,1,1]))  # 3 - WRONG
