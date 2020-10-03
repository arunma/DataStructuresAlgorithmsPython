from typing import List


class PartitionEqualSubsetSum:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        target = sum(nums) // 2

        if sum(nums) & 1 == 1:
            return False

        C = target

        nums.sort()
        dp = [False] * (target + 1)
        dp[0]=True
        for num in nums:
            for csum in range(target + 1):
                if csum>=num:
                    dp[csum] = dp[csum] or dp[csum - num]
                if num<csum:
                    break

        return dp[-1]


if __name__ == '__main__':
    init = PartitionEqualSubsetSum()
    print(init.canPartition([1, 2, 5]))  # false
    print(init.canPartition([1, 2, 3, 4]))  # true
    print(init.canPartition([1, 5, 11, 5]))  # true
    print(init.canPartition([1, 2, 3, 5]))  # false
    print(init.canPartition([1, 2, 3, 4, 5, 6, 7]))  # true
