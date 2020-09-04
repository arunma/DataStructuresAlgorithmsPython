from collections import defaultdict


class BFS:

    def shortestPath(self, connects, start, target, N):
        graph = defaultdict(list)
        for u, v in connects:
            graph[u].append(v)

        visited = [False] * N
        path = self.bfsShowPath(start, target, graph, visited)
        return path

    def bfsDoesPathExist(self, start, target, graph, visited):
        queue = []
        queue.append(start)
        while queue:
            node = queue.pop(0)
            visited[node] = True
            if node ==target:
                return True
            for nei in graph[node]:
                if not visited[nei]:
                    queue.append(nei)

        return False

    def bfsShowPath(self, start, target, graph, visited):
        queue=[[start]]
        while queue:
            path=queue.pop(0)
            node=path[-1]
            visited[node]=True
            if node==target:
                return path
            for nei in graph[node]:
                if not visited[nei]:
                    newpath=list(path)
                    newpath.append(nei)
                    queue.append(newpath)

        return []



if __name__ == '__main__':
    init = BFS()
    connects = [(0, 1), (0, 3), (1, 2), (3, 4), (3, 7), (4, 5), (4, 6), (4, 7), (5, 6), (6, 7)]
    print(init.shortestPath(connects, 0, 7, 8))  # 0,3,7
