from collections import defaultdict
from typing import List

WHITE, GRAY, BLACK = 0, 1, 2


class CourseScheduleII:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)

        seen = [0] * numCourses

        order = []
        for node in range(numCourses):
            #Catch - don't revisit non-white ones
            if seen[node] == WHITE and self.hasCycle(graph, order, seen, node):
                return []

        #Catch - Check for len of topsort result
        if len(order)!=numCourses:
            return []
        return order

    def hasCycle(self, graph, order, seen, node):
        seen[node] = GRAY

        for nei in graph[node]:
            if seen[nei] == GRAY:
                return []
            elif seen[nei] == BLACK:
                continue
            else:
                if self.hasCycle(graph, order, seen, nei):
                    return []

        seen[node] = BLACK
        order.append(node)


if __name__ == "__main__":
    init = CourseScheduleII()
    print(init.findOrder(numCourses = 2, prerequisites = [[1,0]])) #0,1
    print(init.findOrder(numCourses=2, prerequisites=[[0, 1]]))  # 1,0
    print(init.findOrder(numCourses=2, prerequisites=[[0, 1], [1,0]]))  # 1,0
    print(init.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])) #0,1,2,3
