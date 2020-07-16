from collections import Counter
from typing import List


class SingleNumberII:
    def singleNumber(self, nums: List[int]) -> int:
        counter=Counter(nums)
        for ele in counter:
            if counter[ele]==1:
                return ele


if __name__ == '__main__':
    init = SingleNumberII()
    print(init.singleNumber([2,2,3,2]))
    print(init.singleNumber([0,1,0,1,0,1,99]))
