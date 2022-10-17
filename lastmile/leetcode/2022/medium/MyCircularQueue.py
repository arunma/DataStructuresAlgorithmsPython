class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None
        self.prev = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.size == 0:
            self.head = Node(value)
            self.head.next = self.head
            self.head.prev = self.head
            self.tail = self.head
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node
            self.head.prev = node
            node.next = self.head

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            ret_node = self.head
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail

        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


if __name__ == "__main__":
    init = MyCircularQueue(3)
    print(init.enQueue(1))  # return True
    print(init.enQueue(2))  # return True
    print(init.enQueue(3))  # return True
    print(init.enQueue(4))  # return False
    print(init.Rear())  # return 3
    print(init.isFull())  # return True
    print(init.deQueue())  # return True
    print(init.enQueue(4))  # return True
    print(init.Rear())  # return 4
