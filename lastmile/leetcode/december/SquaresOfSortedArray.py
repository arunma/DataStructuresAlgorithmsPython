import collections
from typing import List


class SquaresOfSortedArray:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        result = collections.deque()

        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result.appendleft(nums[left]*nums[left])
                left+=1
            else:
                result.appendleft(nums[right] * nums[right])
                right-=1

        return list(result)


if __name__ == '__main__':
    init = SquaresOfSortedArray()
    print(init.sortedSquares([-4,-1,0,3,10])) #[0,1,9,16,100]
    print(init.sortedSquares([-7,-3,2,3,11])) #[4,9,9,49,121]
