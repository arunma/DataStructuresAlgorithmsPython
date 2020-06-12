import sys
from typing import List


class CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for r in range(1, amount + 1):
            for c in coins:
                if c <= r:
                    dp[r] = min(dp[r], dp[r - c] + 1)

        return -1 if dp[-1] == sys.maxsize else dp[-1]


if __name__ == '__main__':
    init = CoinChange()
    print(init.coinChange(coins=[1, 2, 5], amount=11))  # 3
    print(init.coinChange(coins=[2], amount=3))  # -1
