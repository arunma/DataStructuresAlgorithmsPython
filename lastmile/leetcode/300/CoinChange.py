import sys
from typing import List


class CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        for amt in range(amount + 1):
            for coin in coins:
                if coin <= amt:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        return -1 if dp[-1]==sys.maxsize else dp[-1]


if __name__ == '__main__':
    init = CoinChange()
    print(init.coinChange(coins=[1, 2, 5], amount=11))  # 3
    print(init.coinChange(coins=[2], amount=3))  # -1
