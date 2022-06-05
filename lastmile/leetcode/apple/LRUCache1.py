class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.store={}
        self.first=Node(0,0)
        self.last=Node(0,0)
        self.first.next=self.last
        self.last.prev=self.first
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        else:
            node=self.store[key]
            self.remove(node)
            self.add(node)
            return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.store:
            temp=self.store[key]
            self.remove(temp)

        node = Node(key, value)
        self.add(node)
        self.store[key]=node

        if len(self.store)>self.capacity:
            first_next=self.first.next
            self.remove(first_next)
            del self.store[first_next.key]

    def add (self, node):
        last_prev=self.last.prev
        last_prev.next=node
        node.prev=last_prev
        node.next=self.last
        self.last.prev=node

    def remove(self, node):
        node_prev=node.prev
        node_next=node.next
        node_prev.next=node_next
        node_next.prev=node_prev


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