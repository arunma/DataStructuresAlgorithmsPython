from typing import List


class Subsets:
    def subset(self, nums: List[int]):
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result


if __name__ == '__main__':
    init = Subsets()
    print(init.subset([1, 2, 3]))
