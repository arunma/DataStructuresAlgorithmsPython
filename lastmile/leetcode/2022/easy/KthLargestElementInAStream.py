import heapq
from typing import List


class KthLargestElementInAStream:
    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k=k
        for num in nums:
            heapq.heappush(self.pq, num)
        #Pop all lesser elements. Top is kth element
        while (len(self.pq)>k):
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq)<self.k or val>=self.pq[0]:
            heapq.heappush(self.pq, val)

        if self.pq and len(self.pq)>self.k:
            heapq.heappop(self.pq)

        return self.pq[0]



if __name__ == '__main__':
    # init = KthLargestElementInAStream(3, [4, 5, 8, 2])
    # print(init.add(3))
    # print(init.add(5))
    # print(init.add(10))
    # print(init.add(9))
    # print(init.add(4))

    init = KthLargestElementInAStream(2, [0])
    print(init.add(-1))
    print(init.add(1))
    print(init.add(-2))
    print(init.add(-4))
    print(init.add(3))