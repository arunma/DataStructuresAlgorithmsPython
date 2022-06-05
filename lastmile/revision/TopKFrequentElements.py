import heapq
from collections import Counter
from typing import List


class TopKFrequentElements:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        pq = []
        for key, count in counter.items():
            heapq.heappush(pq, (-count, key))

        result = []
        for _ in range(k):
            if pq:
                count, key = heapq.heappop(pq)
                result.append(key)
        return result


if __name__ == '__main__':
    init = TopKFrequentElements()
    print(init.topKFrequent(nums=[1,1,1,2,2,3], k = 2))
    print(init.topKFrequent(nums = [1], k = 1))
    print(init.topKFrequent(nums = [-1,-1], k = 1))
