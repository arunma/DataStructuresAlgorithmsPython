import collections
from typing import List

class SquaresOfSortedArray:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result=collections.deque()
        left=0
        right=len(A)-1

        while left<=right:
            aleft=abs(A[left])
            aright=abs(A[right])
            if aleft>aright:
                result.appendleft(aleft*aleft)
                left+=1
            else:
                result.appendleft(aright * aright)
                right-=1
        return list(result)




if __name__ == '__main__':
    init = SquaresOfSortedArray()
    print(init.sortedSquares([-4,-1,0,3,10])) #[0,1,9,16,100]
