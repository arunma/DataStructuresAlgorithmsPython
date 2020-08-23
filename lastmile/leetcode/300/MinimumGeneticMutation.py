from collections import defaultdict
from typing import List


'''
Time complexity was O(N * N * M * K) where:

N is length of start string
M is number of letters in gene
K is number of strings in bank
'''
class MinimumGeneticMutation:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = []
        queue.append((start, 0))

        if end not in bank:
            return -1

        visited=defaultdict(bool)
        visited[start]= True

        while queue:
            curr, prevcount = queue.pop(0)
            if curr == end:
                return prevcount
            else:
                for validmut in bank:
                    if self.isViableMutation(curr, validmut) and not visited[validmut]:
                        visited[validmut]=True
                        queue.append((validmut, prevcount+1))

        return -1

    def isViableMutation(self, curr, validmut):
        count=0
        for i, c in enumerate(curr):
            if c!=validmut[i]:
                count+=1
        return count==1

if __name__ == '__main__':
    init = MinimumGeneticMutation()
    print(init.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
    print(init.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
    print(init.minMutation("AAAAAAAA", "CCCCCCCC", ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA"]))
