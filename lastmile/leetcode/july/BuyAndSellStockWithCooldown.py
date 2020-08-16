import sys
from typing import List


class BuyAndSellStockWithCooldown:
    def maxProfit(self, prices: List[int]) -> int:
        sold = float('-inf')
        held = float('-inf')
        reset = 0

        for price in prices:
            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)
        return max(sold, reset)


if __name__ == '__main__':
    init = BuyAndSellStockWithCooldown()
    print(init.maxProfit([1, 2, 3, 0, 2]))
