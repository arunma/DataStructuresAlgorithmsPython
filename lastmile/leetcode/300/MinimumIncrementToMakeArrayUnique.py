from typing import List


class MinimumIncrementToMakeArrayUnique:
    def minIncrementForUnique(self, arr: List[int]) -> int:
        arr.sort()
        result = 0
        for i in range(1, len(arr)):
            prev = arr[i - 1]
            curr = arr[i]
            if prev >= curr:
                result += prev - curr + 1
                arr[i] = prev + 1
        return result


if __name__ == '__main__':
    init = MinimumIncrementToMakeArrayUnique()
    print(init.minIncrementForUnique([1, 2, 2]))  # 1
    print(init.minIncrementForUnique([3, 2, 1, 2, 1, 7]))  # 6
