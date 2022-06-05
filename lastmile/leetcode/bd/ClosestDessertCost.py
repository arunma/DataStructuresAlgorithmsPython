from typing import List


class ClosestDessertCost:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.target=target
        result = 0
        for base in baseCosts:
            result = self.closest (self.dfs(toppingCosts, target, base, 0), result)
        return result

    def closest(self, a, b):
        if not b:
            return a
        if not a:
            return b

        if abs(self.target-a)==abs(self.target-b):
            return a if a<b else b
        elif abs(self.target-a) < abs(self.target-b):
            return a
        else:
            return b


    def dfs(self, toppingCosts, target, curr, index):

        if index>=len(toppingCosts):
            return curr
        noT = self.dfs(toppingCosts, target, curr, index+1)
        oneT = self.dfs(toppingCosts, target, curr+toppingCosts[index], index+1)
        twoT = self.dfs(toppingCosts, target, curr+toppingCosts[index]*2, index+1)

        ans = self.closest(noT, self.closest(oneT, twoT))

        return ans

if __name__ == '__main__':
    init = ClosestDessertCost()
    print(init.closestCost(baseCosts=[1, 7], toppingCosts=[3, 4], target=10))  # 10
    print(init.closestCost(baseCosts=[2, 3], toppingCosts=[4, 5, 100], target=18))  # 17
