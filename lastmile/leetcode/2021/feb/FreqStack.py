import heapq
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.maxheap=[]
        self.cmap=defaultdict(int)
        self.index=0

    def push(self, x: int) -> None:
        self.cmap[x]+=1
        heapq.heappush(self.maxheap, (-self.cmap[x], -self.index, x))
        self.index+=1

    def pop(self) -> int:
        cnt, index, val = cand=heapq.heappop(self.maxheap)
        self.cmap[val]-=1
        if cnt>0:
            heapq.heappush(self.maxheap, (-self.cmap[val], index, val))
        return val


if __name__ == '__main__':
    init = FreqStack()
    print(init.push(5))
    print(init.push(7))
    print(init.push(5))
    print(init.push(7))
    print(init.push(4))
    print(init.push(5))
    print(init.pop()) #5
    print(init.pop()) #7
    print(init.pop()) #5
    print(init.pop()) #4

