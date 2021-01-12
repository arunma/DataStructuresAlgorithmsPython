from typing import List


class KthMissingPositiveNumber:
    def findKthPositive1(self, arr: List[int], k: int) -> int:
        index=0
        for i in range(1,10000):
            if index<len(arr) and arr[index]==i:
                index+=1
            else:
                k-=1

            if k==0:
                return i
        return -1

    def findKthPositive(self, arr: List[int], k: int) -> int:
        low=0
        high=len(arr)-1

        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]-(mid+1)>=k:
                high=mid-1
            else:
                low=mid+1
        return low+k



if __name__ == '__main__':
    init = KthMissingPositiveNumber()
    print(init.findKthPositive(arr = [2,3,4,7,11], k = 5))
    print(init.findKthPositive(arr = [1,2,3,4], k = 2))
