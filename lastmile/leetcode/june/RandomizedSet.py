# class RandomizedSet:
#     def __init__(self):
#         self.store = set()
#
#     def insert(self, val: int) -> bool:
#         if val not in self.store:
#             self.store.add(val)
#             return True
#         return False
#
#     def remove(self, val: int) -> bool:
#         if val in self.store:
#             self.store.remove(val)
#             return True
#         return False
#
#     def getRandom(self) -> int:
#         popped = self.store.pop()
#         self.store.add(popped)
#         return popped
from random import randint


class RandomizedSet:
    def __init__(self):
        self.val_index = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.val_index:
            return False
        else:
            index = len(self.val_index)
            self.val_index[val] = index
            self.vals.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.val_index:
            rm_index = self.val_index[val]
            last_index = len(self.vals) - 1
            last_val = self.vals[last_index]
            self.val_index[last_val] = rm_index  # update dictionary with new index

            del self.val_index[val]  # remove from dictionary
            self.vals[rm_index], self.vals[last_index] = self.vals[last_index], self.vals[rm_index]  # swap before removal
            self.vals.pop()  # remove from list

            return True
        else:
            return False

    def getRandom(self) -> int:
        rm_index = randint(0, len(self.vals) - 1)
        return self.vals[rm_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    randomSet = RandomizedSet()
    print(randomSet.insert(1))  # true
    print(randomSet.remove(2))  # false
    print(randomSet.insert(2))  # true
    print(randomSet.getRandom())  # 1 or 2
    print(randomSet.remove(1))  # true
    print(randomSet.insert(2))  # false - already there
    print(randomSet.getRandom())  # 2
    print()

    randomSet = RandomizedSet()
    print(randomSet.remove(0))  # false
    print(randomSet.remove(0))  # false
    print(randomSet.insert(0))  # true
    print(randomSet.getRandom())  # 0
    print(randomSet.remove(0))  # true
    print(randomSet.insert(0))  # false - already there
