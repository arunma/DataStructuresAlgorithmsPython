import sys


class MinStack:
    # def __init__(self):
    #     self.minValue = sys.maxsize
    #     self.store = []
    #
    # def push(self, x: int) -> None:
    #     if x <= self.minValue:
    #         self.store.append(self.minValue)
    #         self.minValue = x
    #     self.store.append(x)
    #
    # def pop(self) -> None:
    #     if self.store.pop() == self.minValue:
    #         self.minValue = self.store.pop()
    #
    # def top(self) -> int:
    #     return self.store[-1]
    #
    # def getMin(self) -> int:
    #     return self.minValue

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        minValue=self.getMin()
        if minValue==None or x<=minValue:
            minValue=x
        self.stack.append((x, minValue))


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return 0

    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][-1]


if __name__ == '__main__':
    minStack = MinStack()
    # print(minStack.push(3))
    # print(minStack.getMin())  # return 3
    # print(minStack.push(4))
    # print(minStack.push(2))
    # print(minStack.getMin())  # return 3
    # print(minStack.push(6))
    # print(minStack.pop())
    # print(minStack.getMin())  # return 2
    # print(minStack.pop())
    # print(minStack.getMin())  # return 3

    print(minStack.push(0))
    print(minStack.push(1))
    print(minStack.push(0))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.getMin())
