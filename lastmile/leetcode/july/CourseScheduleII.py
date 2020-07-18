from collections import defaultdict
from typing import List


class CourseScheduleII:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[u].append(v)

        top_sort = []

        white = set(range(numCourses))
        gray = set()
        black = set()

        for node in range(numCourses):
            if node in black:
                continue
            elif self.cycle_found(adj_list, white, gray, black, top_sort, node):
                return []

        return top_sort

    def cycle_found(self, adj_list, white, gray, black, top_sort, node):
        white.remove(node)
        gray.add(node)

        for adj in adj_list[node]:
            if adj in black:
                continue
            elif adj in gray:
                return True
            elif self.cycle_found(adj_list, white, gray, black, top_sort, adj):
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
