from typing import List


class ContiguousArray:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        index_map = {0: 0}
        maxCount = 0
        for i, num in enumerate(nums, 1):
            if num == 0:
                count = count - 1
            else:
                count = count + 1

            if count not in index_map:
                index_map[count] = i
            else:
                maxCount = max(maxCount, i - index_map[count])
        return maxCount


if __name__ == '__main__':
    init = ContiguousArray()
    print(init.findMaxLength([0, 1]))  # 2
    print(init.findMaxLength([0, 1, 0]))  # 2
