class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.store={}

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        retnode=self.store[key]
        self.remove(retnode)
        self.add(retnode)
        return retnode.val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])

        node=Node(key, value)
        self.add(node)

        if len(self.store)>self.capacity:
            first=self.head.next
            self.remove(first)

    def add(self, node):
        lastprev=self.tail.prev
        lastprev.next=node
        node.prev=lastprev
        node.next=self.tail
        self.tail.prev=node
        self.store[node.key]=node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        del self.store[node.key]

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