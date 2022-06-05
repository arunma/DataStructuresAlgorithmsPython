from typing import List


class ContinuousSubarraySumMultipleOfK:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixsum = {}
        prefixsum[0] = -1

        currsum = 0
        for i, num in enumerate(nums):
            currsum += num
            modsum = currsum % k

            if modsum in prefixsum:
                if i - prefixsum[modsum] >= 2:
                    return True
            else:
                prefixsum[modsum] = i

        return False


if __name__ == '__main__':
    init = ContinuousSubarraySumMultipleOfK()
    print(init.checkSubarraySum([5,0,0,0], 3))
