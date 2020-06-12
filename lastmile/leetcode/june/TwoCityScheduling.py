from typing import List
import heapq


class TwoCityScheduling:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        half = n // 2
        costs.sort(key=lambda c: c[0] - c[1])
        costs_a1 = sum([a[0] for a in costs[0:half]])
        costs_b1 = sum(b[1] for b in costs[half:])
        sum_a = costs_a1 + costs_b1

        costs.sort(key=lambda c: c[1] - c[0])
        costs_a2 = sum([a[0] for a in costs[0:half]])
        costs_b2 = sum(b[1] for b in costs[half:])
        sum_b = costs_a2 + costs_b2

        return min(sum_a, sum_b)


if __name__ == '__main__':
    init = TwoCityScheduling()
    print(init.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
    print(init.twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))
