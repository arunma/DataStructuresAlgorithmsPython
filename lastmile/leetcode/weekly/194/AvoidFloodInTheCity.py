from itertools import count
from typing import List


class AvoidFloodInTheCity:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        zero_cnt = rains.count(0)
        if zero_cnt == 0:
            return []
        curr = 0
        next = 0
        N = len(rains)
        result = []
        stack = []
        while curr < N:
            if rains[curr] != 0:
                result.append(-1)
                stack.append(rains[curr])
            else:
                if stack:
                    top = stack.pop()
                    result.append(top)
            curr = curr + 1
        return result


if __name__ == '__main__':
    init = AvoidFloodInTheCity()
    print(init.avoidFlood([1, 2, 3, 4])) #[-1,-1,-1,-1]
    print(init.avoidFlood([1, 2, 0, 0, 2, 1])) #[-1,-1,2,1,-1,-1]
    print(init.avoidFlood([1, 2, 0, 1, 2])) #[]
    print(init.avoidFlood([69, 0, 0, 0, 69])) #[-1,69,1,1,-1]
    print(init.avoidFlood([10, 20, 20])) #[]
