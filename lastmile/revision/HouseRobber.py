from typing import List


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        #         odd=0
        #         even=0
        #         for i, num in enumerate(nums):
        #             if i%2==0:
        #                 even+=num
        #             else:
        #                 odd+=num

        #         return max(odd, even)

        N = len(nums)
        if N <= 2:
            return max(nums)

        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]
        dp[2] = nums[1]

        for i in range(3, N + 1):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i - 1]

        return max(dp[-1], dp[-2])

if __name__ == '__main__':
    init = HouseRobber()
    #print(init.rob([2,1,1,2])) #4
    print(init.rob([1,2,3,1])) #4

