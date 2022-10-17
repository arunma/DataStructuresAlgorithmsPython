from collections import defaultdict
from typing import List


class AlienDictionary:
    def alienOrder(self, words: List[str]) -> str:

        def hasCycle(node):
            colors[node] = GRAY
            for nei in graph[node]:
                if colors[nei] == GRAY:
                    return True
                elif colors[nei] == BLACK:
                    continue
                else:
                    if hasCycle(nei):
                        return True

            colors[node] = BLACK
            stack.append(node)
            return False

        if not words:
            return ""

        graph = defaultdict(list)
        for w1, w2 in zip(words, words[1:]):
            if w1!=w2 and w1[:len(w2)]==w2:
                return ''
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[c1].append(c2)
                    break

        colors = defaultdict(int)
        WHITE, GRAY, BLACK = 0, 1, 2

        stack = []

        allnodes=[c for word in words for c in word]

        for node in set(allnodes):
            if colors[node] == WHITE:
                if hasCycle(node):
                    return ''

        return ''.join(reversed(stack))

if __name__ == '__main__':
    init = AlienDictionary()
    print(init.alienOrder(["abc", "ab"])) #""
    print(init.alienOrder([
        "z",
        "z"
    ]))  # zx
    print(init.alienOrder([
        "z",
        "x"
    ]))  # zx
    print(init.alienOrder([
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]))  # wertf

    #print(init.alienOrder(["abc", "ab"]))

    print(init.alienOrder([
        "z",
        "x",
        "z"
    ]))  # ""
