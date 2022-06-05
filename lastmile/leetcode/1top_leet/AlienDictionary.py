from collections import defaultdict
from typing import List

WHITE, GRAY, BLACK = 0, 1, 2

class AlienDictionary:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        stack = []

        for word1, word2 in zip(words, words[1:]):
            if word1 != word2 and len(word2) > len(word1) and word1[:len(word2)] == word2:
                return ''
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    graph[c1].append(c2)
                    break

        colors=defaultdict(int)
        allnodes=[c for word in words for c in word]

        for node in set(allnodes):
            if colors[node]==WHITE:
                if self.hasCycle(node, colors, stack, graph):
                    return ''

        return ''.join(reversed(stack))

    def hasCycle(self, node, colors, stack, graph):
        colors[node]=GRAY
        for nei in graph[node]:
            if colors[nei]==GRAY:
                return True
            elif colors[nei]==BLACK:
                continue
            else:
                if self.hasCycle(nei, colors, stack, graph):
                    return True
        stack.append(node)
        colors[node]=BLACK
        return False



if __name__ == '__main__':
    init = AlienDictionary()
    # print(init.alienOrder(["abc", "ab"]))
    # print(init.alienOrder([
    #     "z",
    #     "z"
    # ]))  # zx
    # print(init.alienOrder([
    #     "z",
    #     "x"
    # ]))  # zx
    print(init.alienOrder([
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]))  # wertf

    # print(init.alienOrder(["abc", "ab"]))
    #
    # print(init.alienOrder([
    #     "z",
    #     "x",
    #     "z"
    # ]))  # ""
