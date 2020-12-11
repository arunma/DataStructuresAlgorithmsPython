import random


class InsertDeleteGetRandomO1:
    def __init__(self):
        self.pos = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.vals.append(val)
            self.pos[val] = len(self.vals) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            index = self.pos[val]
            lastVal = self.vals[-1]

            self.vals[index] = lastVal
            self.pos[lastVal] = index

            self.vals.pop()
            self.pos.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return self.vals[random.randint(0, len(self.vals) - 1)]


if __name__ == '__main__':
    init = InsertDeleteGetRandomO1()
