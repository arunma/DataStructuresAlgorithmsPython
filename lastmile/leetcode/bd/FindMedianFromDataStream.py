import heapq


class FindMedianFromDataStream:
    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        if not self.small or num<=-self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small)-len(self.large)==2:
            top=heapq.heappop(self.small)
            heapq.heappush(self.large, -top)
        elif len(self.large)-len(self.small)>=2:
            top=heapq.heappop(self.large)
            heapq.heappush(self.small, -top)

    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return (-self.small[0]+self.large[0])/2.0

        return -self.small[0] if len(self.small)>len(self.large) else self.large[0]


if __name__ == '__main__':
    medianFinder = FindMedianFromDataStream()
    medianFinder.addNum(1)  # arr = [1]
    medianFinder.addNum(2)  # arr = [1, 2]
    print(medianFinder.findMedian())  # return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3)  # arr[1, 2, 3]
    print(medianFinder.findMedian())  # return 2.0
