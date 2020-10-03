class Node:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

    def __repr__(self):
        return "{}{}".format(self.val, self.right)

class ConvertBinaryTreeToDoublyLinkedList:
    def treeToDoublyList(self, root: Node) -> Node:
        dummy =prev = Node(0)

        node = root
        stack = []

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()

                node.left=prev
                prev.right=node
                prev=prev.right

                node = node.right

        dummy.right.left=prev
        prev.right=dummy.right

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
