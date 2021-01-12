import sys
from typing import List


class StoneGameVII:
    def stoneGameVII(self, stones: List[int]) -> int:
        N=len(stones)
        dp=[[0]* N for _ in range(N)]

        for i in reversed(range(0, N-1)):
            sum=stones[i]
            for j in range(i+1, N):
                sum+=stones[j]
                dp[i][j]=max(sum-stones[i]-dp[i+1][j], sum-stones[j]-dp[i][j-1])

        return dp[0][-1]



if __name__ == '__main__':
    init = StoneGameVII()
    print(init.stoneGameVII([5, 3, 1, 4, 2]))  # 6
    print(init.stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]))  # 122
