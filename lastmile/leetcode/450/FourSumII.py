from collections import defaultdict
from typing import List


class FourSumII:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sumMap=defaultdict(int)
        for a in A:
            for b in B:
                sumMap[a+b]+=1

        result=0
        for c in C:
            for d in D:
                result+=sumMap[-(c+d)]

        return result


if __name__ == '__main__':
    init = FourSumII()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(init.fourSumCount(A, B, C, D))
