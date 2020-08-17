from collections import Counter
from typing import List


class FindDuplicateNumber:
    def findDuplicate(self, nums: List[int]) -> int:
        counter=Counter(nums)
        for k,v in counter.items():
            if v>1:
                return k




if __name__ == '__main__':
    init = FindDuplicateNumber()
    print(init.findDuplicate([1,3,4,2,2])) #2
    print(init.findDuplicate([3,1,3,4,2])) #3

