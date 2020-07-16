from typing import List


class FinalPricesWithSpecialDiscount:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        if not prices:
            return result
        n = len(prices)
        for i in range(n):
            found=False
            for j in range(i + 1, n):
                if prices[j]<=prices[i]:
                    result.append(prices[i]-prices[j])
                    found=True
                    break
            if not found:
                result.append(prices[i])

        return result

if __name__ == '__main__':
    init = FinalPricesWithSpecialDiscount()
    print(init.finalPrices([8, 4, 6, 2, 3]))  # [4,2,4,2,3]
    print(init.finalPrices([1, 2, 3, 4, 5]))
    print(init.finalPrices([10, 1, 1, 6]))  # [9,0,1,6]
