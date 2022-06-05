from collections import defaultdict


class TopSort:

    def topSort(self, nodes, N):
        graph=defaultdict(list)
        for u,v in nodes:
            graph[u].append(v)


        def dfs(node):
            colors[node]=GRAY
            for nei in graph[node]:
                if colors[nei]==GRAY:
                    return False
                elif colors[nei]==WHITE:
                    dfs(nei)
                else:
                    continue
            stack.append(node)
            colors[node]=BLACK
            return True

        stack=[]
        WHITE, GRAY, BLACK=0,1,2
        colors=defaultdict(int)
        for node in range(1,N+1):
            if colors[node]==WHITE:
                if not dfs(node):
                    return set()
        return stack




if __name__ == '__main__':
    init = TopSort()
    print(init.topSort([(1,2),(1,4),(2,4),(2,3),(2,5),(3,5)], 5)) #[4, 5, 3, 2, 1]
