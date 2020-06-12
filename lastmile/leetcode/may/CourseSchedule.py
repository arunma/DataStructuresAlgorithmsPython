from collections import defaultdict
from typing import List, Set


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])

        white=set(range(numCourses))
        gray=set()
        black=set()

        for node in range(numCourses):
            if node in black:
                continue
            if self.isCyleFound(graph, white, black, gray, node):
                return False
        return True

    def isCyleFound(self, graph, white, black, gray, node):
        white.remove(node)
        gray.add(node)

        for adj in graph[node]:
            if adj in black:
                continue
            elif adj in gray:
                return True
            elif self.isCyleFound(graph, white, black, gray, adj):
                return True

        gray.remove(node)
        black.add(node)


if __name__ == '__main__':
    init = CourseSchedule()
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0]]))  # True
    print(init.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))  # False
    print(init.canFinish(numCourses=4, prerequisites=[[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]))  # false
    print(init.canFinish(numCourses=3, prerequisites=[[1, 0], [2, 1]]))  # True
    print(init.canFinish(numCourses=2, prerequisites=[[0, 1]]))  # True
    print(init.canFinish(numCourses=3, prerequisites=[[0,1],[0,2],[1,2]]))  # True
