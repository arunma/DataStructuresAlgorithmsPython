from collections import defaultdict
from typing import List


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)

        for u,v in prerequisites:
            graph[u].append(v)

        WHITE, GRAY, BLACK = 0,1,2
        colors=defaultdict(int)

        def hasCycle(node):
            colors[node]=GRAY
            for v in graph[node]:
                if colors[v]==BLACK:
                    continue
                elif colors[v]==GRAY:
                    return True
                elif colors[v]==WHITE and hasCycle(v):
                    return True
            colors[node]=BLACK
            return False

        for node in range(numCourses):
            if colors[node]==WHITE:
                if hasCycle(node):
                    return False
        return True


if __name__ == '__main__':
    init = CourseSchedule()
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0]]))  # True
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))  # False
