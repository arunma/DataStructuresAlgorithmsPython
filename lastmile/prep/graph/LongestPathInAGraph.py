from collections import defaultdict


class LongestPathInAGraph:

    def longestPathInGraph(self, adj, N):
        graph = defaultdict(list)
        for u, v in adj:
            graph[u].append(v)

        topoSort = self.topSort(graph, 1, N)
        #print("Sort stack -{}".format(topoSort))

        distance = [0] * (N + 1)
        distance[topoSort[-1]] = 0
        diameter=0
        while topoSort:
            current=topoSort.pop()
            diameter = max(diameter, distance[current])
            for nei in graph[current]:
                distance[nei] = max(distance[nei], distance[current] + 1)
        return max(distance) if max(distance)!=N else -1

    def topSort(self, graph, start, N):

        def dfs(graph, visited, node, stack):
            visited[node] = GRAY
            for nei in graph[node]:
                if visited[nei] == WHITE:
                    dfs(graph, visited, nei, stack)

            stack.append(node)
            visited[node] = BLACK

        WHITE, GRAY, BLACK = 0, 1, 2
        visited = defaultdict(int)
        stack = []
        #for node in range(1, N + 1):
        dfs(graph, visited, start, stack)

        return stack


if __name__ == '__main__':
    init = LongestPathInAGraph()
    print(init.longestPathInGraph([(1, 2), (1, 4), (2, 4), (2, 3), (2, 5), (3, 5)], 5))  # #2
    print(init.longestPathInGraph([[1,2],[2,3],[3,1]], 3))  #2
    print(init.longestPathInGraph([[1, 2], [1, 4], [2, 6], [2, 3], [4, 5], [5, 9], [6, 8], [6, 7], [8, 9]], 9)) #4
