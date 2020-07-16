import collections
import sys
from collections import defaultdict
from typing import List


class FindCheapestPrice:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # dist = [sys.maxsize] * n
        # dist[src] = 0
        queue = collections.deque()
        queue.append((src, 0, -1))
        graph = defaultdict(set)
        for u, v, w in flights:
            graph[u].add((v, w))

        dist_dst = sys.maxsize

        while queue:
            node, cost_so_far, stops = queue.popleft()
            if stops > K or cost_so_far > dist_dst:
                continue

            if node == dst:
                dist_dst = min(dist_dst, cost_so_far)

            for nei, wei in graph[node]:
                queue.append((nei, cost_so_far + wei, stops + 1))

        return dist_dst if dist_dst != sys.maxsize else -1


if __name__ == '__main__':
    init = FindCheapestPrice()
    print(init.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=1))  # 200
    print(init.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, K=0))  # 500
    print(init.findCheapestPrice(n=8,
                                 flights=[[3, 4, 7], [6, 2, 2], [0, 2, 7], [0, 1, 2], [1, 7, 8], [4, 5, 2], [0, 3, 2],
                                          [7, 0, 6], [3, 2, 7], [1, 3, 10],
                                          [1, 5, 1], [4, 1, 6], [4, 7, 5], [5, 7, 10]], src=4, dst=3, K=7))  # 500
