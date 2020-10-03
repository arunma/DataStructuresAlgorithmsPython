from typing import List


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        odd_sum=sum(nums[0::2])
        even_sum=sum(nums[1::2])
        return max(odd_sum, even_sum)

    def rob(self, nums: List[int]):
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i+1] = max(nums[i] + dp[i - 1], dp[i])
        return dp[-1]


if __name__ == '__main__':
    init = HouseRobber()
    print(init.rob([1, 2, 3, 1]))  # 4
    print(init.rob([2, 7, 9, 3, 1]))  # 12
    print(init.rob([2, 1, 1, 2]))  # 4
