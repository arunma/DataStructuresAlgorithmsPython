from typing import List


class GasStation:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        gap = 0

        start = 0
        for i in range(len(gas)):
            tank += gas[i]
            if tank < cost[i]:
                gap += cost[i] - tank
                start = i + 1
                tank=0
            else:
                tank-=cost[i]

        if start==len(gas) or tank<gap:
            return -1
        return start


if __name__ == '__main__':
    init = GasStation()
    print(init.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))  # 3
    print(init.canCompleteCircuit(gas=[3,3,4], cost=[3,4,4]))  # -1
    print(init.canCompleteCircuit(gas=[3,1,1], cost=[1,2,2]))  # -1
