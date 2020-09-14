import itertools
from typing import List


class MinimumDeletionCostToAvoidRepeatingLetters:
    # def minCost(self, s: str, cost: List[int]) -> int:
    #     if not s:
    #         return 0
    #     dp = [0] * len(s)
    #
    #     for i in range(1, len(s)):
    #         if s[i]==s[i-1]:
    #             dp[i]=dp[i-1] + min(cost[i], cost[i-1])
    #         else:
    #             dp[i]=dp[i-1]
    #
    #     return dp[-1]

    def minCost(self, s: str, cost: List[int]) -> int:
        ans=i=0
        for k, grp in itertools.groupby(s):
            A=list(grp)
            W=len(A)
            print(A)
            print(W)
            if len(A) == 1:
                i += W
                continue

            m = max(cost[i + j] for j in range(W))
            s = sum(cost[i + j] for j in range(W))
            s -= m
            ans += s
            i += W
        return ans



if __name__ == '__main__':
    init = MinimumDeletionCostToAvoidRepeatingLetters()
    #print(init.minCost(s="abaac", cost=[1, 2, 3, 4, 5]))  # 3
    #print(init.minCost(s="abc", cost=[1, 2, 3]))  # 0
    #print(init.minCost(s="aabaa", cost=[1, 2, 3, 4, 1]))  # 2
    print(init.minCost(s="aaabbbabbbb", cost=[3,5,10,7,5,3,5,5,4,8,1]))  # 26
