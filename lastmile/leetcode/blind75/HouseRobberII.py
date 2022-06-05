from typing import List


class HouseRobberII:
    def rob(self, nums: List[int]) -> int:
        def robin(lst):
            N=len(lst)
            dp=[0]* (N+1)
            dp[1]=lst[0]
            for i in range(2, len(dp)):
                dp[i]=max(lst[i-1]+dp[i-2], dp[i-1])
            return dp[-1]


        return max(robin(nums[:-1]), robin(nums[1:]))

if __name__ == '__main__':
    init = HouseRobberII()
    print(init.rob([1,2,3])) #3
    print(init.rob([2,3,2])) #3
    print(init.rob([1,2,3,1])) #4
