from collections import defaultdict
from typing import List


class SubarraySumEqualsK:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = defaultdict(int)
        prefixsum[0] = 1

        currsum = 0
        result = 0

        for num in nums:
            currsum+=num
            result+=prefixsum[currsum-k]

            prefixsum[currsum]+=1
        return result




if __name__ == '__main__':
    init = SubarraySumEqualsK()
    print(init.subarraySum(nums = [1,1,1], k = 2))
