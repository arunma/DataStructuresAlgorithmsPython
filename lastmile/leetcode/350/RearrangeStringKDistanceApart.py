from collections import Counter
import heapq

#REVISIT
class RearrangeStringKDistanceApart:
    def rearrangeString(self, s: str, k: int) -> str:
        counts = Counter(s)
        pq = []
        [heapq.heappush(pq, (-v, c)) for c, v in counts.items()]

        maxc = max(counts.values())

        result = ''
        while pq:
            n = k + 1
            tempList = []
            while n > 0 and pq:
                n -= 1
                v, c = heapq.heappop(pq)
                result += c
                tempList.append((v + 1, c))

            if len(pq) < k:
                break

            for v, c in tempList:
                if v < 0:
                    heapq.heappush(pq, (v, c))

        return result if len(result) == len(s) else ''


if __name__ == '__main__':
    init = RearrangeStringKDistanceApart()
    print(init.rearrangeString(s="aabbcc", k=3))  # abcabc
    print(init.rearrangeString(s="aaabc", k=3))  # ""
    print(init.rearrangeString(s="aaadbbcc", k=2))  # "abacabcd"
    print(init.rearrangeString("aaabc", 2))  # abaca
