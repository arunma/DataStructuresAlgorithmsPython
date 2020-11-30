class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


class FrontMiddleBackQueue:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def pushFront(self, val: int) -> None:
        nnode = Node(val)
        tail = self.head.next
        nnode.next = tail
        tail.prev = nnode
        self.head.next = nnode

    def pushMiddle(self, val: int) -> None:
        prev = None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        nnode = Node(val)
        prev.next = nnode
        nnode.prev = prev
        nnode.next = slow

    def pushBack(self, val: int) -> None:
        nnode = Node(val)
        head = self.tail.prev
        head.next = nnode
        nnode.prev = head
        nnode.next = self.tail

    def popFront(self) -> int:
        rm = self.head.next
        if rm == self.tail:
            return -1
        else:
            nxt = rm.next
            self.head.next = nxt
            nxt.prev = self.head
        return rm.val

    def popMiddle(self) -> int:
        prev = None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        rm = slow
        prev.next = slow.next
        slow.next.prev = prev
        return rm.val

    def popBack(self) -> int:
        rm = self.tail.prev
        if rm == self.head:
            return -1
        else:
            prev = rm.prev
            self.tail.prev = prev
            prev.next = self.tail


if __name__ == '__main__':
    init = FrontMiddleBackQueue()
    print(init.pushFront(1))
    print(init.pushBack(2))
    print(init.pushMiddle(3))
    print(init.pushMiddle(4))
    print(init.popFront())
    print(init.popMiddle())
    print(init.popMiddle())
    print(init.popBack())
    print(init.popFront())
