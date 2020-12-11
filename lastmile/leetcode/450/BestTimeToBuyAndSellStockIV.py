from typing import List


class BestTimeToBuyAndSellStockIV:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        profits=[0]*len(prices)
        for _ in range(k):
            preprofit=0
            for i in range(1, len(prices)):
                profit=prices[i]-prices[i-1]
                preprofit=max(preprofit+profit, profits[i])
                profits[i]=max(profits[i-1], preprofit)

        return profits[-1]

if __name__ == '__main__':
    init = BestTimeToBuyAndSellStockIV()
    print(init.maxProfit(k = 2, prices = [3,2,6,5,0,3])) #7
