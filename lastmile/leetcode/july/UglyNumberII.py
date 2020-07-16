import heapq


class UglyNumberII:
    def nthUglyNumber(self, n: int) -> int:
        result = []
        result.append(1)
        pq = []
        heapq.heapify(pq)
        for i in range(1, n):
            for el in [2, 3, 5]:
                res = result[i - 1] * el
                if res not in pq:
                    heapq.heappush(pq, res)
            result.append(heapq.heappop(pq))

        return result[-1]


    def nthUglyNumberUgly(self, n: int) -> int:
        result = []
        result.append(1)
        twos = []
        threes = []
        fives = []
        for i in range(1, n):
            twos.append(result[i - 1] * 2)
            threes.append(result[i - 1] * 3)
            fives.append(result[i - 1] * 5)
            _min = min(twos[0], threes[0], fives[0])
            result.append(_min)
            if _min in twos:
                twos.remove(_min)
            if _min in threes:
                threes.remove(_min)
            if _min in fives:
                fives.remove(_min)

        return result[-1]


if __name__ == '__main__':
    init = UglyNumberII()
    print(init.nthUglyNumber(10))  # 12
