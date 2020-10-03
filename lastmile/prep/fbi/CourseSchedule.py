from collections import defaultdict
from typing import List


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def hasCycle(course):
            colors[course] = GRAY
            for nei in graph[course]:
                if colors[nei] == BLACK:
                    continue
                elif colors[nei] == GRAY:
                    return True
                elif hasCycle(nei):
                    return True

            colors[course] = BLACK
            return False

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        WHITE, GRAY, BLACK = 0, 1, 2
        colors = defaultdict(int)
        for course in range(numCourses):
            if colors[course] == WHITE:
                if hasCycle(course):
                    return False
        return True

if __name__ == '__main__':
    init = CourseSchedule()
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0]]))  # True
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))  # False
