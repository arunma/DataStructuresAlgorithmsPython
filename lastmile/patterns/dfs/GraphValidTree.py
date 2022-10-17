from collections import defaultdict
from typing import List


class GraphValidTree:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False

        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        if len(graph)!=n:
            return False
        else:
            visited=set()
            if self.hasCycle(0, -1, graph, visited):
                return False
        return True

    def hasCycle(self, node, parent, graph, visited):
        visited.add(node)
        for nei in graph[node]:
            if nei in visited and nei!=parent:
                return True
            elif nei not in visited:
                if self.hasCycle(nei, node, graph, visited):
                    return True
        return False




if __name__ == '__main__':
    init = GraphValidTree()
    print(init.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]])) #true
    print(init.validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]))#false
    print(init.validTree(4, [[0,1],[2,3]])) #False
