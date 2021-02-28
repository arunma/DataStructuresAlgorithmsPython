from collections import defaultdict
from typing import List


class IsGraphBipartite:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True

        colors = {}
        for node in range(len(graph)):
            if node not in colors:
                colors[node] = 1
            if self.isNeighbourSameColor(node, graph, colors, colors[node]):
                return False
        return True

    def isNeighbourSameColor(self, node, graph, colors, nodeColor):
        for nei in graph[node]:
            if nei in colors and colors[nei] == nodeColor:
                return True
            elif nei not in colors:
                colors[nei] = -nodeColor
                if self.isNeighbourSameColor(nei, graph, colors, colors[nei]):
                    return False
        return False

    # def isBipartite(self, graph: List[List[int]]) -> bool:
    #     if not graph:
    #         return True
    #
    #     colors={0:1}
    #     queue=[(0)]
    #     while queue:
    #         node=queue.pop(0)
    #         for nei in graph[node]:
    #             if nei not in colors:
    #                 colors[nei]=-colors[node]
    #                 queue.append(nei)
    #             elif colors[nei]==colors[node]:
    #                 return False
    #     return True



if __name__ == '__main__':
    init = IsGraphBipartite()
    print(init.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))  # True
    print(init.isBipartite([[1],[0,3],[3],[1,2]]))  # True
    print(init.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))  # False
