from collections import defaultdict
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = defaultdict(int)
        self.sums[-1] = 0
        for i, num in enumerate(nums):
            self.sums[i] += self.sums[i - 1] + num

    def update(self, i: int, val: int) -> None:
        diff=sum[i]
        for i in range(i, len(self.sums)):


    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j] - self.sums[i - 1]


if __name__ == '__main__':
    init = NumArray([1, 3, 5])
    print(init.sumRange(0, 2))  # 8
    init.update(1, 2)
    print(init.sumRange(0, 2))  # 8
