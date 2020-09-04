from collections import defaultdict
from typing import List


class AlienDictionary:
    def alienOrder(self, words: List[str]) -> str:

        def dfs(graph, node, colors, stack):
            colors[node]=GRAY
            for nei in graph[node]:
                if colors[nei]==WHITE:
                    dfs(graph, nei, colors, stack)
            stack.append(node)
            colors[node]=BLACK


        graph=defaultdict(list)

        for word in words:
            for c in word:
                graph[c]=list()

        for i in range(1, len(words)):
            first=words[i-1]
            second=words[i]
            length=min(len(first), len(second))
            for i in range(length):
                if first[i]!=second[i]:
                    graph[first[i]].append(second[i])
                    break


        WHITE, GRAY, BLACK=0,1,2
        colors=defaultdict(int)
        stack=[]
        for node in graph.keys():
            if colors[node]==WHITE:
                dfs(graph, node, colors, stack)
        return ''.join(reversed(stack))




if __name__ == '__main__':
    init = AlienDictionary()
    print(init.alienOrder([
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]))  # wertf

    print(init.alienOrder([
        "z",
        "x"
    ]))  # zx
    print(init.alienOrder([
        "z",
        "x",
        "z"
    ]))  # ""
