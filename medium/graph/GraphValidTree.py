from collections import defaultdict
from typing import List

class GraphValidTree:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        if len(graph)!=n:
            return False

        for node in range(n):
            seen=set()
            if self.hasCycle(graph, seen, node, -1):
                return False
        return True


    def hasCycle(self, graph, seen, node, parent):
        seen.add(node)
        for nei in graph[node]:
            if nei in seen and nei!=parent:
                return True
            elif nei not in seen:
                if self.hasCycle(graph, seen, nei, node):
                    return True
        return False



if __name__ == "__main__":
    init = GraphValidTree()
    print(init.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]])) #true
    print(init.validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]])) #false
