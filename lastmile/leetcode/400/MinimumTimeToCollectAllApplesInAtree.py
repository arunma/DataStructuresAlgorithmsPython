import collections
from typing import List


class MinimumTimeToCollectAllApplesInAtree:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph= collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen=set()
        result=self.dfs(graph, seen, hasApple, 0)
        return max(2*result-2,0)

    def dfs(self, graph, seen, hasApple, node) -> int:
        if node not in seen:
            cost=0
            seen.add(node)
            for nei in graph[node]:
                cost+=self.dfs(graph, seen, hasApple, nei)
            if cost>0 or hasApple[node]:
                return cost+1
        return 0



if __name__ == '__main__':
    init = MinimumTimeToCollectAllApplesInAtree()
    print(init.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]))
