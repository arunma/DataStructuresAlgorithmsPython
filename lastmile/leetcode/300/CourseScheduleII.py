from collections import defaultdict
from typing import List


class CourseScheduleII:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.construct_adj_list(prerequisites)

        white=set(range(numCourses))
        gray=set()
        black=set()

        top_sort=[]

        for node in range(numCourses):
            if node in black:
                continue
            elif self.hasCycle(node, graph, top_sort, white, gray, black):
                return []
        return top_sort



    def construct_adj_list(self, prerequisites):
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        return graph

    def hasCycle(self, node, graph, top_sort, white, gray, black):
        white.remove(node)
        gray.add(node)

        for u in graph[node]:
            if u in black:
                continue
            if u in gray:
                return True
            elif self.hasCycle(u, graph, top_sort, white, gray, black):
                return True

        top_sort.append(node)
        gray.remove(node)
        black.add(node)
        return False


if __name__ == '__main__':
    init = CourseScheduleII()
    print(init.findOrder(2, [[1, 0]]))  # [0,1]
    print(init.findOrder(2, [[0, 1]]))  # [1,0]
    print(init.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0,1,2,3] or [0,2,1,3]
