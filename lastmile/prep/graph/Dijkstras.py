import heapq
import sys
from collections import defaultdict


class Dijkstras:

    def find_shortest(self, adjs, N):
        graph = defaultdict(list)
        for u, v, w in adjs:
            graph[u].append((v, w))

        distance = [sys.maxsize] * N
        distance[0] = 0
        pq = [[0, 0]]  # cost, node
        visited = [False] * N
        while pq:
            curr_dist, node = heapq.heappop(pq)
            visited[node] = True
            for nei, nei_cost in graph[node]:
                if not visited[nei]:
                    distance[nei] = min(distance[nei], curr_dist + nei_cost)
                    heapq.heappush(pq, (distance[nei], nei))
        return distance

if __name__ == '__main__':
    init = Dijkstras()
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
