import random
from typing import List


class ShuffleAnArray:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.store = nums.copy()

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        for i in range(len(self.store)):
            randind = random.randrange(i, len(self.store))
            self.store[i], self.store[randind] = self.store[randind], self.store[i]
        return self.store


if __name__ == '__main__':
    init = ShuffleAnArray(nums=[1, 2, 3])
    print(init.shuffle())
    print(init.reset())  # [1,2,3]
    print(init.shuffle())
