import functools
from typing import List


class CompStr(str):
    def __lt__(self, that):
        return self + that < that + self


class LargestNumber:
    def largestNumber(self, nums: List[int]) -> str:
        snums = [str(num) for num in nums]
        snums.sort(key=CompStr, reverse=True)
        return ''.join(snums).lstrip('0') or '0'


if __name__ == '__main__':
    init = LargestNumber()
    print(init.largestNumber([10, 2]))
    print(init.largestNumber([3, 30, 34, 5, 9]))
