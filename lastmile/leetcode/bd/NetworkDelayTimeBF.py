import heapq
import sys
from collections import defaultdict
from typing import List


class NetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        dists=[sys.maxsize]*(n+1)
        dists[0]=0
        dists[k]=0

        for node in range (1, n):
            for nei, wei in graph[node]:
                if dists[node]+wei<dists[nei]:
                    dists[nei]=dists[node]+wei


        for node in range (1, n):
            for nei, wei in graph[node]:
                if dists[node]+wei<dists[nei]:
                    print("has negative cycle")

        return max(dists)








if __name__ == '__main__':
    init = NetworkDelayTime()
    print(init.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)) #2
    print(init.networkDelayTime(times = [[1,2,1]], n = 2, k = 1)) #1
    print(init.networkDelayTime(times = [[1,2,1]], n = 2, k = 2)) #-1
