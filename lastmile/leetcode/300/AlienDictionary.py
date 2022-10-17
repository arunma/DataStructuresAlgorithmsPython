from collections import defaultdict
from typing import List


class AlienDictionary:
    # def alienOrder(self, words: List[str]) -> str:
    #
    #     def dfs(graph, node, colors, stack):
    #         colors[node]=GRAY
    #         for nei in graph[node]:
    #             if colors[nei]==WHITE:
    #                 dfs(graph, nei, colors, stack)
    #         stack.append(node)
    #         colors[node]=BLACK
    #
    #
    #     graph=defaultdict(list)
    #
    #     for word in words:
    #         for c in word:
    #             graph[c]=list()
    #
    #     for i in range(1, len(words)):
    #         first=words[i-1]
    #         second=words[i]
    #         length=min(len(first), len(second))
    #         for i in range(length):
    #             if first[i]!=second[i]:
    #                 graph[first[i]].append(second[i])
    #                 break
    #
    #
    #     WHITE, GRAY, BLACK=0,1,2
    #     colors=defaultdict(int)
    #     stack=[]
    #     for node in graph.keys():
    #         if colors[node]==WHITE:
    #             dfs(graph, node, colors, stack)
    #     return ''.join(reversed(stack))
    #

    # def alienOrder(self, words: List[str]) -> str:
    #
    #     def dfs(graph, node):
    #         colors[node] = GRAY
    #         for adj in graph[node]:
    #             if colors[adj] == WHITE:
    #                 if dfs(graph, adj):
    #                     return True
    #             elif colors[adj] == BLACK:
    #                 continue
    #             elif colors[adj] == GRAY:
    #                 return True
    #         colors[node] = BLACK
    #         stack.append(node)
    #         return False
    #
    #     graph = {}
    #
    #     for word in words:
    #         for c in word:
    #             graph[c] = []
    #
    #     for i in range(1, len(words)):
    #         prev = words[i - 1]
    #         curr = words[i]
    #         if len(prev) > len(curr) and prev[:len(curr)] == curr:
    #             return ''
    #         for j in range(min(len(prev), len(curr))):
    #             if prev[j] != curr[j]:
    #                 graph[prev[j]].append(curr[j])
    #                 break
    #
    #     WHITE, GRAY, BLACK = 0, 1, 2
    #     colors = defaultdict(int)
    #
    #     stack = []
    #
    #     for node in graph.keys():
    #         if colors[node] == WHITE:
    #             if dfs(graph, node):
    #                 return ''
    #
    #     return ''.join(reversed(stack))

    WHITE, GRAY, BLACK = 0, 1, 2


    def alienOrder(self, words: List[str]) -> str:

        graph = {}

        for word in words:
            for c in word:
                graph[c] = []

        wordPairs = zip(words, words[1:])

        for word1, word2 in wordPairs:
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ''
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    graph[c1].append(c2)
                    break

        colors = defaultdict(int)
        stack = []
        for node in graph.keys():
            if colors[node] == self.WHITE:
                if self.hasCycle(graph, colors, stack, node):
                    return ""

        stack.reverse()
        return ''.join(stack)

    def hasCycle(self, graph, colors, stack, node):
        colors[node] = self.GRAY
        for nei in graph[node]:
            if colors[nei] == self.WHITE:
                if (self.hasCycle(graph, colors, stack, nei)):
                    return True
            elif colors[nei] == self.GRAY:
                return True
            elif colors[nei] == self.BLACK:
                continue

        stack.append(node)
        colors[node] = self.BLACK
        return False


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

    print(init.alienOrder(["aac", "aabb", "aaba"]))
