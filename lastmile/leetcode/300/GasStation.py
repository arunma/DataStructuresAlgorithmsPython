from typing import List


class GasStation:
    # https://leetcode.com/problems/gas-station/discuss/167542/10-lines-Python-that-beats-100-NO-PROOF-IN-HERE
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        gap = start = tank = 0
        for i in range(N):
            tank += gas[i]
            if tank >= cost[i]:
                tank -= cost[i]
            else:
                gap += cost[i] - tank
                start = i + 1
                tank = 0
        if start == N or tank < gap:
            return -1
        return start


if __name__ == '__main__':
    init = GasStation()
    print(init.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))  # 3
    '''
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    '''
    print(init.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))  # -1
    '''
    gas  = [2,3,4]
    cost = [3,4,3]
    '''
    print(init.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]))  # 4
