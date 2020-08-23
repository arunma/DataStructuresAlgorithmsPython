import heapq
from collections import defaultdict, Counter
from typing import List


class MostVisitedSectorInACircularTrack:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        count = defaultdict(int)

        curr = rounds[0]
        for i in range(1, len(rounds)):
            while curr != rounds[i]:
                print("curr {}, rounds[i]{}".format(curr,rounds[i]))
                count[curr] += 1
                curr += 1
                if curr > n:
                    curr = 1
        count[curr] += 1

        mx = max(count.values())
        return sorted([k for k, v in count.items() if v == mx])


if __name__ == '__main__':
    init = MostVisitedSectorInACircularTrack()
    print(init.mostVisited(n=4, rounds=[1, 3, 1, 2]))
    print(init.mostVisited(n=2, rounds=[2, 1, 2, 1, 2, 1, 2, 1, 2]))  # [2]
