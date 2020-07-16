import collections
import sys
from collections import defaultdict
from typing import List
import heapq


class Dijkstras:
    def find_shortest(self, conns: List[List[int]], n: int) -> List[int]:
        graph = defaultdict(set)
        for frm, to, w in conns:
            graph[frm].add((to, w))
        seen = set()
        dist = [sys.maxsize] * n
        dist[0] = 0

        pq = [(0, 0)]  # cost,src
        while pq:
            curr_cost, curr = heapq.heappop(pq)
            if curr in seen:
                continue
            seen.add(curr)
            for nei, neic in graph[curr]:
                dist[nei] = min(dist[nei], curr_cost + neic)
                heapq.heappush(pq, (dist[nei], nei))
        return dist


if __name__ == '__main__':
    init = Dijkstras()
    # conn = [
    #     [0, 2, 8],
    #     [1, 2, 9],
    #     [1, 5, 8],
    #     [2, 0, 8],
    #     [2, 1, 9],
    #     [2, 4, 6],
    #     [3, 5, 1],
    #     [3, 7, 8],
    #     [4, 2, 6],
    #     [4, 7, 1],
    #     [5, 1, 8],
    #     [5, 3, 1],
    #     [5, 7, 2],
    #     [6, 7, 5],
    #     [7, 3, 8],
    #     [7, 4, 1],
    #     [7, 5, 2],
    #     [7, 6, 5],
    # ]
    conn = [
        [0, 1, 3],
        [0, 2, 2],
        [1, 2, 8],
        [1, 5, 2],
        [2, 4, 7],
        [3, 1, 9],
        [3, 5, 1],
        [5, 7, 1],
        [6, 2, 6],
        [6, 4, 7],
        [7, 5, 7],
        [7, 6, 2],
    ]
    print(init.find_shortest(conn, 8))
    # print(init.networkDelayTime(conn, 8, 0))
