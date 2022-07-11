import heapq


class UglyNumbers:
    def nthUglyNumber(self, n: int) -> int:
        pq=[1]

        for i in range(1, n):
            top = heapq.heappop(pq)
            while pq and top==pq[0]:
                heapq.heappop(pq)

            heapq.heappush(pq, top*2)
            heapq.heappush(pq, top*3)
            heapq.heappush(pq, top*5)

        return pq[0]






if __name__ == '__main__':
    init = UglyNumbers()
    #print(init.nthUglyNumber(10))
    print(init.nthUglyNumber(11))
    print(init.nthUglyNumber(1))
