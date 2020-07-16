import collections
from typing import List


class LastMomentBeforeAllAntsFallOut:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res=0
        for l in left:
            res=max(l, res)
        for r in right:
            res=max(n-r, res)
        return res


if __name__ == '__main__':
    init = LastMomentBeforeAllAntsFallOut()
    print(init.getLastMoment(n=4, left=[4, 3], right=[0, 1])) #4
    print(init.getLastMoment(n=7, left=[], right=[0, 1, 2, 3, 4, 5, 6, 7])) #7
    print(init.getLastMoment(n=7, right=[], left=[0, 1, 2, 3, 4, 5, 6, 7])) #7
    print(init.getLastMoment(n=9, left=[5], right=[4])) #5
    print(init.getLastMoment(n=6, left=[6], right=[0])) #6
