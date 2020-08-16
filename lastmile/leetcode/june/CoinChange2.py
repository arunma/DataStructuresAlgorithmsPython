from typing import List


class CoinChange2:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for a in range(amount + 1):
                if c <= a:
                    dp[a] = dp[a - c] + dp[a]
        return dp[-1]


if __name__ == '__main__':
    init = CoinChange2()
    print(init.change(5, [1, 2, 5]))
