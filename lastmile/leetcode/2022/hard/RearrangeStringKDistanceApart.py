import heapq
from collections import Counter


class RearrangeStringKDistanceApart:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        counter = Counter(s)

        pq = []
        for c, count in counter.items():
            heapq.heappush(pq, (-count, c))

        result = ''
        waitlist = []

        while pq:
            mcount, c = heapq.heappop(pq)
            result += c
            mcount += 1
            waitlist.append((mcount, c))

            if len(waitlist)<k:
                continue
            else:
                tcount, tc = waitlist.pop(0)
                if tcount<0:
                    heapq.heappush(pq, (tcount, tc))

        return result if len(result) == len(s) else ''


if __name__ == '__main__':
    init = RearrangeStringKDistanceApart()
    print(init.rearrangeString(s="aabbcc", k=3))  # abcabc
    print(init.rearrangeString(s="aaabc", k=3))  #
    print(init.rearrangeString(s="aaadbbcc", k=2))  # abacabcd
    print(init.rearrangeString(s="a", k=0))  # a
    print(init.rearrangeString(s="abb", k=2))  # bab
    print(init.rearrangeString("vvlov", k=2))
