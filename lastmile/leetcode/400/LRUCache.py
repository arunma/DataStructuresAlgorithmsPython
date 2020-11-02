class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        node = self.store[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, val: int) -> None:

        if key in self.store:
            temp = self.store[key]
            self.remove(temp)

        node = Node(key, val)
        self.add(node)
        self.store[key] = node

        if len(self.store) > self.cap:
            top = self.head.next
            self.remove(top)
            del self.store[top.key]

    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def remove(self, n):
        prev = n.prev
        next = n.next
        prev.next = next
        next.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # returns 1
    cache.put(3, 3)  # evicts key 2
    print(cache.get(2))  # returns - 1(not found)
    cache.put(4, 4)  # evicts  key  1
    print(cache.get(1))  # returns - 1(not found)
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4
    # 1,-1,-1,3,4