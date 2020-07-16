class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self):
        return str(self.val) + "->" + (str(self.next) if self.next else "")



class FlattenAMultilevelDoublyLinkedList:
    def flatten(self, head: Node) -> Node:

        if not head:
            return head

        result = Node(0,None,head,None)
        prev = result

        stack = []
        stack.append(head)

        while stack:
            node = stack.pop()
            prev.next = node
            node.prev = prev

            if node.next:
                stack.append(node.next)
                node.next = None

            if node.child:
                stack.append(node.child)
                node.child = None
            prev = node

        result.next.prev=None
        return result.next


if __name__ == '__main__':
    init = FlattenAMultilevelDoublyLinkedList()

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six

    three.child = seven
    seven.next = eight
    eight.next = nine
    nine.next = ten

    eight.child = eleven
    eleven.next = twelve

    print(init.flatten(one))
