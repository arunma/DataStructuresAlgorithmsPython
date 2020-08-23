from collections import defaultdict
from typing import List


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.construct_adjacency_list(prerequisites)
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)

        def hasCycle(graph, color, node):
            color[node] = GRAY
            for u in graph[node]:
                if color[u] == BLACK:
                    continue
                elif color[u] == WHITE:
                    if hasCycle(graph, color, u):
                        return True
                elif color[u] == GRAY:
                    return True
            color[node] = BLACK
            return False

        for node in range(numCourses):
            if color[node] == WHITE:
                if hasCycle(graph, color, node):
                    return False

        return True

    def construct_adjacency_list(self, prerequisites):
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        return graph


if __name__ == '__main__':
    init = CourseSchedule()
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0]]))  # True
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))  # False
