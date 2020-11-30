from collections import defaultdict
from typing import List


class MaxWealth:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        balance=defaultdict(int)
        for i, bal in enumerate(accounts):
            balance[i]+=sum(bal)

        return max(balance.values())


if __name__ == '__main__':
    init = MaxWealth()
    print(init.maximumWealth([[1,2,3],[3,2,1]]))
    print(init.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))
