from collections import defaultdict
from typing import List


class MinimumNumberOfVerticesToReachAllNodes:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        deg = [0] * n
        for u, v in edges:
            deg[v] += 1
        return [i for i, v in enumerate(deg) if deg[i] == 0]

    # def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    #     graph=defaultdict(list)
    #     for u,v in edges:
    #         graph[u].append(v)
    #
    #     visited=set()
    #     result = set()
    #     for node in range(n):
    #         if node not in visited:
    #             result.add(node)
    #             self.dfs(node, visited, graph, result)
    #     return list(result)
    #
    # def dfs(self, node, visited, graph, result):
    #     visited.add(node)
    #     for u in graph[node]:
    #         if u in result:
    #             result.remove(u)
    #         if u not in visited:
    #             self.dfs(u, visited, graph, result)


if __name__ == '__main__':
    init = MinimumNumberOfVerticesToReachAllNodes()
    print(init.findSmallestSetOfVertices(n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))  # [0,3]
    print(init.findSmallestSetOfVertices(n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))  # [0,2. 3]
    print(init.findSmallestSetOfVertices(n=3, edges=[[1, 2], [1, 0], [0, 2]]))  # [1]
