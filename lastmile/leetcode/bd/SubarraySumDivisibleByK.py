from collections import defaultdict
from typing import List


class SubarraySumDivisibleByK:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixsum=defaultdict(int)
        prefixsum[0]=1

        result=0
        currsum=0
        for num in nums:
            currsum+=num
            prefixsum[currsum%k]+=1


        return result


if __name__ == '__main__':
    init = SubarraySumDivisibleByK()
    print(init.subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5)) #7

