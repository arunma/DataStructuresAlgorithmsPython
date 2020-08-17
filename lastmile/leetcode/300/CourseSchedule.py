from collections import defaultdict
from typing import List


class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=self.construct_adjacency_list(prerequisites)
        white=set(range(numCourses))

        gray=set()
        black=set()
        for node in range(numCourses):
            if node in black:
                continue
            elif self.hasCycle(node, graph, white, gray, black):
                return False
        return True

    def construct_adjacency_list(self, prerequisites):
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        return graph

    def hasCycle(self, node, graph, white, gray, black):
        white.remove(node)
        gray.add(node)

        for u in graph[node]:
            if u in black:
                continue
            elif u in gray:
                return True
            elif self.hasCycle(u, graph, white, gray, black):
                return True
        gray.remove(node)
        black.add(node)

if __name__ == '__main__':
    init = CourseSchedule()
    print(init.canFinish(numCourses = 2, prerequisites = [[1,0]])) #True
    print(init.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]])) #False
