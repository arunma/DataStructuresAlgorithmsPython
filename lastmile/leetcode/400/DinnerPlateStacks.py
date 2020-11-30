import heapq


class DinnerPlateStacks:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.queue=[]
        self.stacks=[]

    def push(self, val: int) -> None:
        while self.queue and self.queue[0]<len(self.stacks) and len(self.stacks[self.queue[0]])==self.capacity:
            heapq.heappop(self.queue)

        if not self.queue:
            self.stacks.append([])
            heapq.heappush(self.queue, len(self.stacks))

        if self.queue[0]==len(self.stacks):
            self.stacks.append([])

        self.stacks[self.queue[0]].append(val)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return self.popAtStack(len(self.stacks)-1)

    def popAtStack(self, index: int) -> int:
        if -1<index<len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.queue, index)
            return self.stacks[index].pop()
        return -1

if __name__ == '__main__':
    init = DinnerPlateStacks(2)
    print(init.push(1))
    print(init.push(2))
    print(init.push(3))
    print(init.push(4))
    print(init.push(5))
    print(init.popAtStack(0))
    print(init.push(20))
    print(init.push(21))
    print(init.popAtStack(0))
    print(init.popAtStack(0))
    print(init.pop())
    print(init.pop())
    print(init.pop())
    print(init.pop())
    print(init.pop())
