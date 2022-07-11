from collections import defaultdict
from typing import List


class IsGraphBipartite:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True

        colors = {}
        for node in range(len(graph)):
            if node not in colors:
                colors[node]=1
            if not self.areNeighboursValidColor(node, colors[node], graph, colors):
                return False
        return True


    # def areNeighboursValidColor(self, pnode, pcolor, graph, colors):
    #     for nei in graph[pnode]:
    #         if nei in colors and colors[nei]==pcolor:
    #             return False
    #         elif nei not in colors:
    #             colors[nei]=-pcolor
    #             if not self.areNeighboursValidColor(nei, colors[nei], graph, colors):
    #                 return False
    #     return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True

        colors={}

        for node in range(len(graph)):
            if node in colors:
                continue

            if node not in colors:
                colors[node]=1
            queue=[node]

            while queue:
                cnode=queue.pop(0)
                for nei in graph[cnode]:
                    if nei in colors and colors[nei]==colors[cnode]:
                        return False
                    elif nei not in colors:
                        colors[nei]=-colors[cnode]
                        queue.append(nei)
        return True





if __name__ == '__main__':
    init = IsGraphBipartite()
    print(init.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))  # True
    print(init.isBipartite([[1],[0,3],[3],[1,2]]))  # True
    print(init.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))  # False
