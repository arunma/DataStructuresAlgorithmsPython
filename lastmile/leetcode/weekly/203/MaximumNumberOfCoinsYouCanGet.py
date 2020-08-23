from typing import List


class MaximumNumberOfCoinsYouCanGet:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        bobs=len(piles)//3
        piles=piles[:-bobs]
        return sum(piles[1::2])


if __name__ == '__main__':
    init = MaximumNumberOfCoinsYouCanGet()
    print(init.maxCoins([2,4,1,2,7,8])) #9
    print(init.maxCoins([2,4,5])) #4
    print(init.maxCoins([9,8,7,6,5,1,2,3,4])) #18
