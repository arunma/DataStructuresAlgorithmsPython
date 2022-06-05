from collections import defaultdict
from typing import List


class BurstBalloons:
    # def maxCoins(self, nums: List[int]) -> int:
    #     nums = [1] + nums + [1]
    #     dp = defaultdict(int)
    #
    #     def dfs(l, r):
    #         if l > r:
    #             return 0
    #         if (l, r) in dp:
    #             return dp[(l, r)]
    #         for i in range(l, r + 1):
    #             coins = nums[l - 1] * nums[i] * nums[r + 1]
    #             coins += dfs(l, i - 1) + dfs(i + 1, r)
    #             dp[(l, r)] = max(dp[(l, r)], coins)
    #         return dp[(l, r)]
    #
    #     return dfs(1, len(nums) - 2)

    def maxCoins(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        self.dfs(nums, dp)
        return max(dp.values())

    def dfs(self, nums, dp):
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif tuple(nums) in dp:
            return dp[tuple(nums)]

        localmax=0
        for i in range(len(nums)):
            coins = nums[i]
            if i - 1 < 0:
                coins *= 1
            else:
                coins *= nums[i - 1]

            if i + 1 > len(nums) - 1:
                coins *= 1
            else:
                coins *= nums[i + 1]
            localmax=max(localmax, coins + self.dfs(nums[:i]+nums[i+1:], dp))
            dp[tuple(nums)]=localmax
        return localmax


if __name__ == '__main__':
    init = BurstBalloons()
    print(init.maxCoins([3, 1, 5, 8]))
