class MyHashSet:
    def __init__(self):
        self.store = [False] * 1000001

    def add(self, key: int) -> None:
        self.store[key]=True

    def remove(self, key: int) -> None:
        self.store[key]=False

    def contains(self, key: int) -> bool:
        return self.store[key]


if __name__ == '__main__':
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    print(hashSet.contains(1))  # returns   true
    print(hashSet.contains(3))  # returns false(not found)
    hashSet.add(2)
    print(hashSet.contains(2))  # returns   true
    hashSet.remove(2)
    print(hashSet.contains(2))  # returns false(already removed)
