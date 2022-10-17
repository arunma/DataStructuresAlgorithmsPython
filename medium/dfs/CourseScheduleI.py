from collections import defaultdict
from typing import List


WHITE, GRAY, BLACK = 0, 1, 2
class CourseScheduleI:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        seen = [0] * numCourses

        for node in range(numCourses):
            if self.hasCycle(graph, seen, node):
                return False
        return True

    def hasCycle(self, graph, seen, node):
        seen[node] = GRAY

        for nei in graph[node]:
            if seen[nei] == GRAY:
                return True
            elif seen[nei] == BLACK:
                continue
            else:
                if self.hasCycle(graph, seen, nei):
                    return True

        seen[node] = BLACK
        return False


if __name__ == "__main__":
    init = CourseScheduleI()
    print(init.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]])) #False
    print(init.canFinish(numCourses = 2, prerequisites = [[1,0]])) #True
