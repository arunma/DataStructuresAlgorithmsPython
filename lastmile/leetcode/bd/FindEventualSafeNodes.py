from collections import defaultdict
from typing import List

WHITE, GRAY, BLACK = 0, 1, 2
class FindEventualSafeNodes:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)

        terms = []
        colors = defaultdict(int)
        for node in range(N):
            if not self.has_cycle(node, graph, colors):
                terms.append(node)

        terms.sort()
        return terms

    def has_cycle(self, node, graph, colors):
        colors[node] = GRAY
        for nei in graph[node]:
            if colors[nei] == BLACK:
                continue
            elif colors[nei] == GRAY:
                return True
            else:
                if self.has_cycle(nei, graph, colors):
                    return True

        colors[node] = BLACK
        return False


if __name__ == '__main__':
    init = FindEventualSafeNodes()
    print(init.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])) #2456
