from collections import defaultdict


class TopologicalSort:
    def topSort(self, adj, N):
        def dfs(graph, top_stack, visited, node):
            visited[node]=GRAY
            for nei in graph[node]:
                if visited[nei]==WHITE:
                    dfs(graph, top_stack, visited, nei)
            top_stack.append(node)
            visited[node]=BLACK

        graph=defaultdict(list)
        for u,v in adj:
            graph[u].append(v)

        WHITE, GRAY, BLACK=0,1,2
        top_stack=[]
        visited=defaultdict(int)
        for node in range(1, N+1):
            if visited[node]==WHITE:
                dfs(graph, top_stack, visited, node)
        return top_stack


if __name__ == '__main__':
    init = TopologicalSort()
    print(init.topSort([(1,2),(1,4),(2,4),(2,3),(2,5),(3,5)], 5)) #[4, 5, 3, 2, 1]
