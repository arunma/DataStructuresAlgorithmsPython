import heapq
from collections import defaultdict, Counter
from typing import List


class TopKFrequentElements:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq=[]
        heapq.heapify(pq)
        freq_map=Counter(nums)
        for key, val in freq_map.items():
            heapq.heappush(pq, (-val, key))

        result=[]
        for _ in range(k):
            result.append(heapq.heappop(pq)[1])
        return result

    def topKFrequentM(self, nums: List[int], k: int) -> List[int]:
        pq=[]
        heapq.heapify(pq)
        freq_map=defaultdict(int)
        for num in nums:
            freq_map[num]+=1

        for key, val in freq_map.items():
            heapq.heappush(pq, (-val, key))

        result=[]
        for _ in range(k):
            result.append(heapq.heappop(pq)[1])
        return result



if __name__ == '__main__':
    init = TopKFrequentElements()
    print(init.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print(init.topKFrequent(nums = [1], k = 1))
