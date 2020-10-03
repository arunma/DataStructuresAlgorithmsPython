import random
from typing import List


class RandomPickIndex:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        result = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randint(1, count) == count:
                    result = i

        return result


if __name__ == '__main__':
    init = RandomPickIndex([1,2,3,3,3])
    print(init.pick(3)) #2,3 or 4
    print(init.pick(1)) #0
