import heapq
from collections import Counter


class ReorganizeString:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)

        pq = []
        for c, count in counter.items():
            heapq.heappush(pq, (-count,c))

        if -pq[0][0] > len(s)//2+1:
            return ""

        result = ''
        temp = []

        while pq:
            mcount, c = heapq.heappop(pq)
            result += c

            while temp:
                tmcount, tc = temp.pop()
                heapq.heappush(pq, (tmcount, tc))

            mcount += 1
            if mcount != 0:
                temp.append((mcount, c))

        return result if len(result)==len(s) else ''

if __name__ == '__main__':
    init = ReorganizeString()
    print(init.reorganizeString("aab")) #aba
    print(init.reorganizeString("aaab")) #""
    print(init.reorganizeString("vvvlo")) #"vlvov"
    print(init.reorganizeString("aaab")) #""
