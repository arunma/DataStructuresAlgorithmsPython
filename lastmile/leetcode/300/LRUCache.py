import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.store = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.store:
            self.store.move_to_end(key)
            return self.store[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.store[key] = value
        self.store.move_to_end(key)

        if len(self.store) > self.capacity:
            self.store.popitem(last=False)


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
