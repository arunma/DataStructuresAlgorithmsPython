import sys
from collections import Counter, defaultdict
from typing import List


class OptimalAccountBalancing:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        counter = defaultdict(int)
        for f, t, am in transactions:
            counter[f] -= am
            counter[t] += am

        balances = list(counter.values())
        return self.settle(balances, 0)

    def settle(self, balances, start):
        while start < len(balances) and balances[start] == 0:
            start += 1

        if start == len(balances):
            return 0

        result = float('inf')
        for i in range(start + 1, len(balances)):
            if balances[i] * balances[start] < 0:
                balances[i] += balances[start]
                result = min(result, 1 + self.settle(balances, start + 1))
                balances[i] -= balances[start]

        return result


if __name__ == '__main__':
    init = OptimalAccountBalancing()
    print(init.minTransfers([[0, 1, 10], [2, 0, 5]]))  # 2
    print(init.minTransfers([[2, 0, 5], [3, 4, 4]]))  # 2
    print(init.minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))  # 1
