from collections import defaultdict
from typing import List


WHITE,GRAY,BLACK=0,1,2

class CourseScheduleII:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)


        colors=defaultdict(int)
        stack=[]
        for n in range(numCourses):
            if colors[n]==WHITE:
                if self.hasCycle(graph, n, colors, stack):
                    return []
        return list(stack)


    def hasCycle(self, graph, node, colors, stack):
        colors[node]=GRAY

        for nei in graph[node]:
            if colors[nei]==GRAY:
                return True
            elif colors[nei]==BLACK:
                continue
            else:
                if self.hasCycle(graph, nei, colors, stack):
                    return True

        stack.append(node)
        colors[node]=BLACK
        return False





if __name__ == '__main__':
    init = CourseScheduleII()
    print(init.findOrder(2, [[1, 0]]))  # [0,1]
    print(init.findOrder(2, [[0, 1]]))  # [1,0]
    print(init.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0,1,2,3] or [0,2,1,3]
    print(init.findOrder(2, [[1, 0], [0,1]]))  # [0,1]

