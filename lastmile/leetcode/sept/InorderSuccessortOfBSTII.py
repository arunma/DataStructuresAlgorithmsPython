class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class InorderSuccessortOfBSTII:
    def inorderSuccessor(self, node: Node) -> Node:
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr

        while node.parent and node.parent.val < node.val:
            node = node.parent
        return node.parent


def fromString(vals):
    root = Node(vals[0])
    queue = [root]
    index = 1
    while queue:
        node = queue.pop(0)
        if index < len(vals) and vals[index]:
            node.left = Node(vals[index])
            queue.append(node.left)
        index += 1
        if index < len(vals) and vals[index]:
            node.right = Node(vals[index])
            queue.append(node.right)
        index += 1
    return root


if __name__ == '__main__':
    init = InorderSuccessortOfBSTII()
    root = fromString([2, 1, 3])
    print(init.inorderSuccessor(root.left))  # 2
    root = fromString([5, 3, 6, 2, 4, None, None, 1])
    print(init.inorderSuccessor(root.right))  # null
    root = fromString([15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, None, None, None, None, None, 9])
    print(init.inorderSuccessor(root))  # 17
    root = fromString([15, 6, 18, 3, 7, 17, 20, 2, 4, None, 13, None, None, None, None, None, None, None, None, 9])
    print(init.inorderSuccessor(root.left.right.right))  # 15
