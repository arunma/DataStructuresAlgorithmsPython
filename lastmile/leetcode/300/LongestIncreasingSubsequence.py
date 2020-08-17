from typing import List


class LongestIncreasingSubsequence:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N=len(nums)
        dp=[1]*N
        for i in range(N):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i], dp[j]+1)
        return max(dp)

if __name__ == '__main__':
    init = LongestIncreasingSubsequence()
    print(init.lengthOfLIS([10,9,2,5,3,7,101,18])) #4
    print(init.lengthOfLIS([1,3,6,7,9,4,10,5,6])) #6
