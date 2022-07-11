from collections import defaultdict
from typing import List


class NumberOfProvinces:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0

        seen=set()
        for node in range(len(isConnected)):
            if node not in seen:
                self.dfs(node, isConnected, seen)
                provinces+=1

        return provinces


    def dfs(self, node, graph, seen):
        seen.add(node)
        for nei, adj in enumerate(graph[node]):
            if adj and nei not in seen:
                self.dfs(nei, graph, seen)





if __name__ == '__main__':
    init = NumberOfProvinces()
    print(init.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])) #2
    print(init.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])) #3
    print(init.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])) #1
