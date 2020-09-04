from collections import defaultdict


class CloneAGraph:
    def cloneGraph(self, connects, N):
        def cloneChildren(graph, node, visited, node_lookup, new_graph):
            visited[node] = GRAY
            for nei in graph[node]:
                if nei not in node_lookup:
                    node_lookup[nei] = nei
                nei_node = node_lookup[nei]
                new_graph[node].append(nei_node)
                if visited[node] == WHITE:
                    cloneChildren(graph, nei, visited, node_lookup, new_graph)
            visited[node]=BLACK

        WHITE, GRAY, BLACK = 0, 1, 2
        graph = defaultdict(list)
        for u, v in connects:
            graph[u].append(v)

        visited = defaultdict(int)
        node_lookup = {}
        new_graph = defaultdict(list)
        for node in range(N):
            node_lookup[node] = node
            cloneChildren(graph, node, visited, node_lookup, new_graph)
        return new_graph


if __name__ == '__main__':
    init = CloneAGraph()
    connects = [(0, 1), (0, 3), (1, 2), (3, 4), (3, 7), (4, 5), (4, 6), (4, 7), (5, 6), (6, 7)]
    print(init.cloneGraph(connects, 8))  # {0: [1, 3], 1: [2], 3: [4, 7], 4: [5, 6, 7], 5: [6], 6: [7]})
