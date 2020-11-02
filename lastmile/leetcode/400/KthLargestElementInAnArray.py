import heapq
from typing import List


class KthLargestElementInAnArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]
        for num in nums:
            heapq.heappush(pq, num)

        for i in range (len(nums)-k):
            heapq.heappop(pq)

        return heapq.heappop(pq)

if __name__ == '__main__':
    init = KthLargestElementInAnArray()
    print(init.findKthLargest([3,2,1,5,6,4], k = 2)) #5
