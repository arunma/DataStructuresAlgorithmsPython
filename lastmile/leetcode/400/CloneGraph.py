class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class CloneGraph:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue = [node]
        copy = {node: Node(node.val)}
        while queue:
            curr = queue.pop(0)

            for nei in curr.neighbors:
                if nei not in copy:
                    copy[nei] = Node(nei.val)
                    queue.append(nei)
                copy[curr].neighbors.append(copy[nei])

        return copy[node]


if __name__ == '__main__':
    init = CloneGraph()
