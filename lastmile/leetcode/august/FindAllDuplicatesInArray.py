from collections import Counter, defaultdict
from typing import List


class FindAllDuplicatesInArray:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        for k,v in counter.items():
            if v > 1:
                result.append(k)
        return result

    # def findDuplicates(self, nums: List[int]) -> List[int]:
    #     freq = defaultdict(int)
    #     result = []
    #     for num in nums:
    #         freq[num] += 1
    #
    #     for k, v in freq.items():
    #         if v > 1:
    #             result.append(k)
    #     return result


if __name__ == '__main__':
    init = FindAllDuplicatesInArray()
    print(init.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # 2,3
