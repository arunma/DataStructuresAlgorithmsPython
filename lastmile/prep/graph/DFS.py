from collections import defaultdict


class DFS:

    # def doesPathExist(self, adj, start, target, N):
    #     graph=defaultdict(list)
    #     for u,v in adj:
    #         graph[u].append(v)
    #     visited=[False] *N
    #     return self.dfs(start, target, graph,visited)
    #
    # def dfs(self, node, target, graph, visited):
    #     visited[node]=True
    #     if node==target:
    #         return True
    #     for nei in graph[node]:
    #         if not visited[nei]:
    #             if (self.dfs(nei, target, graph, visited)):
    #                 return True
    #     return False

    def doesPathExist(self, adj, start, target, N):

        def dfs (node, target):
            colors[node]=GRAY
            if node==target:
                return True
            for nei in graph[node]:
                if colors[nei]==WHITE:
                    if (dfs(nei, target)):
                        return True
            colors[node]=BLACK




        graph=defaultdict(list)
        for u,v in adj:
            graph[u].append(v)

        colors = defaultdict(int)
        WHITE, GRAY, BLACK = 0, 1, 2
        if dfs(start, target):
            return True
        return False



if __name__ == '__main__':
    init = DFS()
    connects = [(0, 1), (0, 3), (1, 2), (3, 4), (3, 7), (4, 5), (4, 6), (4, 7), (5, 6), (6, 7)]
    print(init.doesPathExist(connects, 0, 7, 8))  # 0,3,7
    print(init.doesPathExist(connects, 4, 2, 8))  # 0,3,7
