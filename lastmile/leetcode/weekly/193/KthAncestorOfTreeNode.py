from typing import List


class KthAncestorOfTreeNode:

    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        self.n = n

    def getKthAncestor(self, node: int, k: int) -> int:
        search = node
        while k > 1:
            search = self.parent[search] #key
            k -= 1
            if search == -1:
                return -1
        else:
            return self.parent[search] #key


if __name__ == '__main__':
    init = KthAncestorOfTreeNode(7, [-1, 0, 0, 1, 1, 2, 2])
    print(init.getKthAncestor(3, 1))  # 1
    print(init.getKthAncestor(5, 2))  # 0
    print(init.getKthAncestor(6, 3))  # -1

    init = KthAncestorOfTreeNode(5, [-1, 0, 0, 1, 2])
    print(init.getKthAncestor(3, 5))  # -1
    print(init.getKthAncestor(3, 2))  # 0
    print(init.getKthAncestor(2, 2))  # -1
    print(init.getKthAncestor(0, 2))  # -1
    print(init.getKthAncestor(2, 1))  # 0
