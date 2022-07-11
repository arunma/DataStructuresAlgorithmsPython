class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val) + "->" + (str(self.right) if self.right else "")
        
class ConvertBinarySearchTreeToSortedDoublyLinkedList:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        sent = Node(0)
        head = sent

        stack = []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                lnode = Node(node.val)

                head.right = lnode
                lnode.left = head
                head = head.right

                node = node.right

        head.right=sent.right
        sent.right.left=head
        return sent.right

if __name__ == '__main__':
    init = ConvertBinarySearchTreeToSortedDoublyLinkedList()
    root = Node(4)
    root.left = Node(2)
    root.left.right = Node(3)
    root.left.left = Node(1)
    root.right = Node(5)
    print(init.treeToDoublyList(root))
