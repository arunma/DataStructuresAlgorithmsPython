from math import log, log2
from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        heightOfTree=int(log2(n)+1)
        self.parents=[[-1] * n for _ in range(heightOfTree)]
        for i in range(n):
            self.parents[0][i]=parent[i]

        for i in range(1, heightOfTree):
            for node in range (n):
                nodeParent=self.parents[i-1][node]
                if nodeParent!=-1:
                    self.parents[i][node]=self.parents[i-1][nodeParent]

        for each in self.parents:
            print(each)




    def getKthAncestor(self, node: int, k: int) -> int:
        pass


if __name__ == '__main__':
    init = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    #print(init.getKthAncestor(3, 1))  # 1
    #print(init.getKthAncestor(5, 2))  # 0
    #print(init.getKthAncestor(6, 3))  # -1
