import heapq
from collections import defaultdict
from typing import List


class ReconstructItinerary:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        #for u, v in sorted(tickets)[::-1]:
        for u, v in tickets:
            graph[u].append(v)

        self.route = []
        self.visit("JFK", graph)
        return self.route[::-1]

    def visit(self, v, graph):
        while graph[v]:
            self.visit(graph[v].pop(), graph)
        self.route.append(v)


if __name__ == '__main__':
    init = ReconstructItinerary()
    print(init.findItinerary(
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))  # ["JFK", "MUC", "LHR", "SFO", "SJC"]
    print(init.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"],
                              ["ATL", "SFO"]]))  # ["JFK","ATL","JFK","SFO","ATL","SFO"]
