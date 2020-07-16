import collections
from collections import defaultdict
from math import inf
from typing import List


class FindTwoNonOverlappingSubarraysEachWithTargetSum:

    # def minSumOfLengths0(self, arr: List[int], target: int) -> int:
    #     n = len(arr)
    #     i = j = 0
    #     s = 0
    #     cand = collections.defaultdict(lambda: float('inf'))
    #     ret = float('inf')
    #     while j < n:
    #         s += arr[j]
    #         j += 1
    #         cand[j] = cand[j - 1]
    #         if s == target:
    #             cand[j] = min(cand[j], j - i)
    #             ret = min(ret, j - i + cand[i])
    #         while s > target:
    #             s -= arr[i]
    #             i += 1
    #         if s == target:
    #             cand[j] = min(cand[j], j - i)
    #             ret = min(ret, j - i + cand[i])
    #     return -1 if ret == float('inf') else ret
    #
    def minSumOfLengths1(self, arr: List[int], target: int) -> int:
        record = defaultdict(lambda: inf)
        bestprev = inf
        j = 0
        total = 0
        ret = inf
        for i, x in enumerate(arr):
            total += x
            while total > target:
                total -= arr[j]
                bestprev = min(bestprev, record[j])
                j += 1

            if total == target:
                record[i] = i - j + 1
                ret = min(ret, bestprev + record[i])

        if ret == inf:
            ret = -1

        return ret

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        j = 0
        record = defaultdict(lambda: float('inf'))
        cumsum = 0
        ret = float('inf')
        bestprev = float('inf')
        for i, item in enumerate(arr):
            cumsum += item
            record[i] = record[i - 1]
            while cumsum > target:
                cumsum -= arr[j]
                bestprev = min(bestprev, record[j])
                j += 1
            if cumsum == target:
                record[i] = i - j + 1
                ret = min(ret, bestprev + record[i])
        if ret==float('inf'):
            return -1
        else:
            return ret


if __name__ == '__main__':
    init = FindTwoNonOverlappingSubarraysEachWithTargetSum()
    # print(init.minSumOfLengths(arr=[3, 2, 2, 4, 3], target=3))  # 2
    print(init.minSumOfLengths(arr=[7, 3, 4, 7], target=7))  # 2
    print(init.minSumOfLengths(arr=[4, 3, 2, 6, 2, 3, 4], target=6))  # -1
    print(init.minSumOfLengths(arr=[5, 5, 4, 4, 5], target=3))  # -1
    print(init.minSumOfLengths(arr=[3, 1, 1, 1, 5, 1, 2, 1], target=3))  # 3
    print(init.minSumOfLengths(arr=[1, 2, 2, 3, 2, 6, 7, 2, 1, 4, 8], target=5))  # 4
    print(init.minSumOfLengths(arr=[2, 3, 2, 2, 1, 4, 8], target=5))  # 4
