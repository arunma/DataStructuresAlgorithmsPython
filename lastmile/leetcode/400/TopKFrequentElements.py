import heapq
from collections import Counter
from typing import List


class TopKFrequentElements:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter=Counter(nums)
    #     pq=[]
    #     for num, count in counter.items():
    #         heapq.heappush(pq, (-count, num))
    #
    #     result=[]
    #     for i in range(k):
    #         count, num =heapq.heappop(pq)
    #         result.append(num)
    #     return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        counter = Counter(nums)

        for k, count in counter.items():
            heapq.heappush(pq, (-count, k))

        result = []
        for i in range(k):
            if pq:
                count, key = heapq.heappop(pq)
                result.append(key)
        return result

if __name__ == '__main__':
    init = TopKFrequentElements()
    print(init.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print(init.topKFrequent(nums = [1], k = 1))
