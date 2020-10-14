from typing import List


class PartitionEqualSubsetSum:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        target = sum(nums) // 2

        if sum(nums) & 1 == 1:
            return False

        C = target

        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for csum in range(target + 1):
                if csum >= num:
                    dp[csum] = dp[csum] or dp[csum - num]

        return dp[-1]


if __name__ == '__main__':
    init = PartitionEqualSubsetSum()
    print(init.canPartition([3,3,3,4,5])) #True
    print(init.canPartition([1,2,5])) #False
