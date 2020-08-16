from typing import List


class HIndex:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h=1
        i=0
        while i<len(citations) and h<=citations[i]:
            i+=1
            h+=1
        return h-1



if __name__ == '__main__':
    init = HIndex()
    print(init.hIndex([3, 0, 6, 1, 5]))  # 3
    print(init.hIndex([]))  # 0
    print(init.hIndex([1]))  # 1
