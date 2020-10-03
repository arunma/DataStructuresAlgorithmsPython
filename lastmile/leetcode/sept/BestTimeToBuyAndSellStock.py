import sys
from typing import List


class BestTimeToBuyAndSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxProfit=0
        minValue=prices[0]
        for price in prices[1:]:
            maxProfit=max(maxProfit, price-minValue)
            minValue=min(minValue, price)
        return maxProfit



if __name__ == '__main__':
    init = BestTimeToBuyAndSellStock()
    print(init.maxProfit([7,1,5,3,6,4])) #5
    print(init.maxProfit([7,6,4,3,1])) #0
