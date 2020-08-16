import heapq
from typing import List


class KthLargestElementArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]

        for num in nums:
            heapq.heappush(pq, num)
            if len(pq)>k:
                heapq.heappop(pq)
        return pq[0]



if __name__ == '__main__':
    init = KthLargestElementArray()
    print(init.findKthLargest([3, 2, 1, 5, 6, 4], k=2)) #5
    print(init.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))#4
