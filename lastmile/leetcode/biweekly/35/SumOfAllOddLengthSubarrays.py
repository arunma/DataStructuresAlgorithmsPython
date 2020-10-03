from typing import List
import itertools as it
from itertools import tee


class SumOfAllOddLengthSubarrays:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        totalSum=sum(arr)
        for size in range(3, len(arr)+1, 2):
            for each in self.window(arr, size):
                totalSum+=sum(list(each))
        return totalSum

    def window(self, iterable, size):
        iters = tee(iterable, size)
        for i in range(1, size):
            for each in iters[i:]:
                next(each, None)
        return zip(*iters)




if __name__ == '__main__':
    init = SumOfAllOddLengthSubarrays()
    print(init.sumOddLengthSubarrays([1,4,2,5,3]))

