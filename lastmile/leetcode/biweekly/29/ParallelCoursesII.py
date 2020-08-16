from collections import defaultdict
from typing import List


class ParallelCoursesII:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        V = n
        for u, v in dependencies:
            graph[u].append(v)
        stack = []
        visited = [False] * (V + 1)
        for v in range(1, V + 1):
            if not visited[v]:
                self.topologicalSort(v, graph, visited, stack)

        index = stack.index(n)
        slice = stack[0:index + 1]

        div, mod = divmod(len(slice), k)
        return div + 1

    def topologicalSort(self, v, graph, visited, lst):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                self.topologicalSort(u, graph, visited, lst)

        lst.insert(0, v)


if __name__ == '__main__':
    init = ParallelCoursesII()
    print(init.minNumberOfSemesters(n=4, dependencies=[[2, 1], [3, 1], [1, 4]], k=2))  # 3
    print(init.minNumberOfSemesters(n=5, dependencies=[[2, 1], [3, 1], [4, 1], [1, 5]], k=2))  # 4
    print(init.minNumberOfSemesters(n=11, dependencies=[], k=2))  # 6
