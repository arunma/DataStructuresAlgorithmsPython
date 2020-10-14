from collections import defaultdict
from typing import List


class MaximalNetworkRank:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0
        graph =defaultdict(list)
        for u,v in roads:
            graph[u].append(v)

        self.counts=defaultdict(int)
        for i in range(n):
            colors=defaultdict(int)
            if not graph[i]:
                continue
            self.dfs(graph, i, i, colors)

        maxCounts=max(self.counts.values())
        return 1 if maxCounts==2 else maxCounts

    def dfs(self, graph, src, node, colors):
        WHITE, GRAY, BLACK=0,1,2
        colors[node]=GRAY
        for nei in graph[node]:
            if colors[nei]==WHITE:
                self.dfs(graph, src, nei, colors)
            elif colors[nei]==BLACK:
                continue

        self.counts[src]+=1
        colors[node]=BLACK






if __name__ == '__main__':
    init = MaximalNetworkRank()
    print(init.maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]])) #4
    print(init.maximalNetworkRank(n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])) #5
    print(init.maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]])) #5
    print(init.maximalNetworkRank(n = 2, roads = [[1,0]])) #5


