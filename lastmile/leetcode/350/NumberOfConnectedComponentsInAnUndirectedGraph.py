from collections import defaultdict
from typing import List


class NumberOfConnectedComponentsInAnUndirectedGraph:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        components = 0
        for node in range(n):
            if node not in seen:
                self.dfs(graph, seen, node)
                components += 1

        return components

    def dfs(self, graph, seen, node):
        seen.add(node)
        for nei in graph[node]:
            if nei not in seen:
                self.dfs(graph, seen, nei)


if __name__ == '__main__':
    init = NumberOfConnectedComponentsInAnUndirectedGraph()
    print(init.countComponents(n = 5 , edges = [[0, 1], [1, 2], [3, 4]])) #2
