import sys
from typing import List


class BuyAndSellStockIII:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2=sys.maxsize,sys.maxsize
        profit1, profit2=0,0

        for price in prices:
            buy1=min(buy1, price)
            profit1=max(profit1, price-buy1)

            buy2=min(buy2, price-profit1)
            profit2=max(profit2, price-buy2)

        return profit2

    def maxProfit1(self, prices: List[int]) -> int:

        N = len(prices)

        dp = [[0] * N for _ in range(3)]

        for k in range(1, 3):
            minPrice = prices[0]
            for i in range(1, len(prices)):
                currMin = min(minPrice, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - currMin)

        return dp[-1][-1]





if __name__ == '__main__':
    init = BuyAndSellStockIII()
    print(init.maxProfit(prices = [3,3,5,0,0,3,1,4])) #6
    #print(init.maxProfit(prices = [1,2,3,4,5])) #4
    #print(init.maxProfit(prices = [7,6,4,3,1])) #0
