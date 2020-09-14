import collections


class MovingAverageOfDataStream:
    def __init__(self, size: int):
        self.size = size
        self.store = collections.deque()
        self.sum=0


    def next(self, val: int) -> float:
        self.sum+=val
        self.store.append(val)
        if len(self.store)>self.size:
            going=self.store.popleft()
            self.sum-=going
        return self.sum/len(self.store)



if __name__ == '__main__':
    m = MovingAverageOfDataStream(3)
    print(m.next(1))  # = 1
    print(m.next(10))  # = (1 + 10) / 2
    print(m.next(3))  # = (1 + 10 + 3) / 3
    print(m.next(5))  # = (10 + 3 + 5) / 3

