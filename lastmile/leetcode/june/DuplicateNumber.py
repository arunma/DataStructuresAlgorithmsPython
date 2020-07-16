from typing import List


class DuplicateNumber:
    def findDuplicate(self, nums: List[int]) -> int:
        already=set()
        for num in nums:
            if num in already:
                return num
            already.add(num)
        return -1

if __name__ == '__main__':
    init = DuplicateNumber()
    print(init.findDuplicate([1,3,4,2,2]))
