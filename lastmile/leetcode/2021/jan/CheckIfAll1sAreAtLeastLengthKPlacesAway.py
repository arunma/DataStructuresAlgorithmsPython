import heapq
from typing import List


class CheckIfAll1sAreAtLeastLengthKPlacesAway:
    # def kLengthApart(self, nums: List[int], k: int) -> bool:
    #     pq=[]
    #     for i, num in enumerate(nums):
    #         if num==1:
    #             if pq and i+pq[0]<=k:
    #                 return False
    #             heapq.heappush(pq, -i)
    #     return True

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        maxIndex=-1
        for i, num in enumerate(nums):
            if num==1:
                if maxIndex!=-1 and (i-maxIndex)-1<k:
                    return False
                maxIndex=i
        return True

if __name__ == '__main__':
    init = CheckIfAll1sAreAtLeastLengthKPlacesAway()
    print(init.kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2))
    print(init.kLengthApart(nums = [1,0,0,1,0,1], k = 2))
