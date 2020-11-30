class Node:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}{}".format(self.val, self.right)

class ConvertBinaryTreeToDoublyLinkedList:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = []
        head = dummy = Node(0)

        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                head.right = node
                node.left = head
                head = head.right

                node = node.right

        head.right = dummy.right
        dummy.right.left = head
        return dummy.right

if __name__ == '__main__':
    init = ConvertBinaryTreeToDoublyLinkedList()
    four = Node(4)
    two = Node(2)
    one = Node(1)
    three = Node(3)
    five = Node(5)

    four.left=two
    two.left=one
    two.right=three
    four.right=five

    print(init.treeToDoublyList(four))
