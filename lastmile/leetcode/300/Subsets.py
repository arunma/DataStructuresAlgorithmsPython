from typing import List


class Subsets:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        result = [curr]
        for num in nums:
            for i in range(len(result)):
                result.append(result[i].copy()+[num])
        return result


if __name__ == '__main__':
    init = Subsets()
    print(init.subsets([1, 2, 3]))
