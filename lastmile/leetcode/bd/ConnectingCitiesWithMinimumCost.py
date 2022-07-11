import heapq
from collections import defaultdict
from typing import List


class ConnectingCitiesWithMinimumCost:

    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in connections:
            graph[u].append((v, w))
            graph[v].append((u, w))

        pq = [(0, 1)]
        seen = set()
        cost = 0

        while pq:
            w, node = heapq.heappop(pq)
            if node not in seen:
                seen.add(node)
                cost += w

                for nei, wei in graph[node]:
                    if nei not in seen:
                        heapq.heappush(pq, (wei, nei))

        return cost if len(seen) == n else -1

    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        pq=[]
        graph=defaultdict(list)
        for u,v,w in connections:
            graph[u].append((v,w))
            graph[v].append((u,w))

        heapq.heappush(pq, (0,1))

        result=[]
        visited=[False]*(n+1)

        while pq:
            w,u=heapq.heappop(pq)
            if not visited[u]:
                result.append(w)
                visited[u]=True
                for v,w in graph[u]:
                    if not visited[v]:
                        heapq.heappush(pq, (w,v))

        if len(result)==n:
            return sum(result)
        else:
            return -1








if __name__ == '__main__':
    init = ConnectingCitiesWithMinimumCost()
    print(init.minimumCost(n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]])) #6
    print(init.minimumCost(n = 4, connections = [[1,2,3],[3,4,4]])) #-1
