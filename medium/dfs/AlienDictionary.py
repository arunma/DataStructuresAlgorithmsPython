from collections import defaultdict
from typing import List

WHITE, GRAY, BLACK=0,1,2
class AlienDictionary:
    def alienOrder(self, words: List[str]) -> str:
        graph=defaultdict(list)

        for word1, word2 in zip(words, words[1:]):
            if word1!=word2 and word1[:len(word2)]==word2:
                return ""
            for c1, c2 in zip(word1, word2):
                if c1==c2:
                    continue
                else:
                    graph[c1].append(c2)
                    break

        #print(graph)
        allnodes=[c for word in words for c in word]

        result=[]

        colors=defaultdict(int)
        for node in set(allnodes):
            if colors[node]==WHITE:
                if self.hasCycle(graph, node, colors, result):
                    return ""

        return ''.join(reversed(result))

    def hasCycle(self, graph, node, colors, result):
        colors[node]=GRAY
        for nei in graph[node]:
            if colors[nei] == GRAY:
                return True
            elif colors[nei] == BLACK:
                continue
            else:
                if self.hasCycle(graph, nei, colors, result):
                    return True
        colors[node]=BLACK
        result.append(node)
        return False

if __name__ == "__main__":
    init = AlienDictionary()

    print(init.alienOrder([
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]))  # wertf

    print(init.alienOrder(["abc", "ab"]))
    print(init.alienOrder([
        "z",
        "z"
    ]))  # zx
    print(init.alienOrder([
        "z",
        "x"
    ]))  # zx
    print(init.alienOrder(["zy", "zx"])) #yxz

    print(init.alienOrder([
        "z",
        "x",
        "z"
    ]))  # ""
