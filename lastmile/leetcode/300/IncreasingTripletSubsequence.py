import sys
from typing import List


class IncreasingTripletSubsequence:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False
        first = sys.maxsize
        second = sys.maxsize

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


if __name__ == '__main__':
    init = IncreasingTripletSubsequence()
    print(init.increasingTriplet([1, 2, 3, 4, 5]))  # True
    print(init.increasingTriplet([5, 4, 3, 2, 1]))  # False
    print(init.increasingTriplet([1, 4, 3, 2, 1]))  # False
