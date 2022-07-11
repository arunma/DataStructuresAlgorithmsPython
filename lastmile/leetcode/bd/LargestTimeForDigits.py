import itertools
from typing import List


class LargestTimeForDigits:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        perms = itertools.permutations(arr)
        print(list(perms))



if __name__ == '__main__':
    init = LargestTimeForDigits()
    print(init.largestTimeFromDigits(arr = [1,2,3,4]))
