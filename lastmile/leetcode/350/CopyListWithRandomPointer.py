class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        return str(self.val) + "->" + (str(self.next) if self.next else "")


class CopyListWithRandomPointer:
    def copyRandomList(self, head: Node) -> Node:
        node=head
        copy={}

        while node:
            copy[node]=Node(node.val)
            node=node.next

        node=head

        while node:
            copy[node].next=copy.get(node.next)
            copy[node].random=copy.get(node.random)
            node=node.next

        return copy.get(head)


if __name__ == '__main__':
    init = CopyListWithRandomPointer()
    seven = Node(7)
    thirteen = Node(13)
    eleven = Node(11)
    ten = Node(10)
    one = Node(1)

    seven.next = thirteen
    thirteen.next = eleven
    eleven.next = ten
    ten.next = one

    seven.random=None
    thirteen.random=seven
    eleven.random=one
    ten.random=eleven
    one.random=seven

    print(init.copyRandomList(seven))
