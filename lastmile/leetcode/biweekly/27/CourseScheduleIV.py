from typing import List


class CourseScheduleIV:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for i in range(n)]
        for c, p in prerequisites:
            graph[c].append(p)

        ans = []
        for c, t in queries:
            stack = [c]
            seen = {c}
            while stack:
                curr = stack.pop()
                if curr == t:
                    ans.append(True)
                    break
                for nei in graph[curr]:
                    if nei not in seen:
                        stack.append(nei)
                        seen.add(curr)
            else:
                stack.append(False)

        return ans


if __name__ == '__main__':
    init = CourseScheduleIV()
    print(
        init.checkIfPrerequisite(n=3, prerequisites=[[1, 2], [1, 0], [2, 0]], queries=[[1, 0], [1, 2]]))  # [true,true]
    print(init.checkIfPrerequisite(n=3, prerequisites=[[1, 0], [2, 0]], queries=[[0, 1], [2, 0]]))  # [false,true]
    print(init.checkIfPrerequisite(n=5, prerequisites=[[0, 1], [1, 2], [2, 3], [3, 4]],
                                   queries=[[0, 4], [4, 0], [1, 3], [3, 0]]))  # [true,false,true,false]
