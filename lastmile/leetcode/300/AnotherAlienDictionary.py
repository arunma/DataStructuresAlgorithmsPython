from collections import defaultdict
from typing import List


class AnotherAlienDictionary:
    def alienOrder(self, words: List[str]) -> str:
        '''
        1. Compare the previous word with the current word
        2. If they are different add an edge from prev to current
        3. If they are same, continue

        End goal: Topsort
        '''
        def dfs(graph, node, colors, stack):
            colors[node] = GRAY
            for nei in graph[node]:
                if colors[nei] == BLACK:
                    continue
                elif colors[nei] == GRAY:
                    return True
                elif colors[nei] == WHITE:
                    if dfs(graph, nei, colors, stack):
                        return True

            stack.append(node)
            colors[node] = BLACK
            return False

        graph = defaultdict(list)

        for i in range(1, len(words)):
            pword = words[i - 1]
            cword = words[i]
            for j in range(min(len(pword), len(cword))):
                if pword[j] != cword[j]:
                    graph[pword[j]].append(cword[j])
                    break

        colors = defaultdict(int)
        WHITE, GRAY, BLACK = 0, 1, 2
        # Top sort graph
        stack = []
        for node in set(graph.keys()):
            if colors[node] == WHITE:
                if dfs(graph, node, colors, stack):
                    return ""

        return ''.join(reversed(stack))


if __name__ == '__main__':
    init = AnotherAlienDictionary()
    print (init.alienOrder(["abc","ab"]))
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

