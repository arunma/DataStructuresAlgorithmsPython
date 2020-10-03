from typing import List


class ContinuousSubarraySum:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixDict = {0: -1}

        currSum = 0
        for i, num in enumerate(nums):
            currSum += num

            if k != 0:
                currSum = currSum % k

            if currSum in prefixDict:
                prev = prefixDict[currSum]
                if i - prev > 1:
                    return True

            else:
                prefixDict[currSum] = i
        return False


if __name__ == '__main__':
    init = ContinuousSubarraySum()
    print(init.checkSubarraySum([23, 2, 4, 6, 7],  k=6)) #2,4
    print(init.checkSubarraySum([23, 2, 6, 4, 7],  k=6)) #23,2,6,4,7
    print(init.checkSubarraySum([0,0],  k=0))
