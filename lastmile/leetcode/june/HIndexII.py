from typing import List


class HIndexII:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        N = len(citations) - 1
        for i in range(len(citations)):
            if citations[i] >= (N - i + 1):
                return N - i + 1
        return 0

    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        N = len(citations)
        low, high = 0, N - 1
        while low <= high:
            mid = (low + high) // 2
            if citations[mid] >= (N - mid):
                high = mid - 1
            else:
                low = mid + 1

        return N - low


if __name__ == '__main__':
    init = HIndexII()
    print(init.hIndex(citations=[0, 1, 3, 5, 6]))  # 3
    print(init.hIndex(citations=[3, 4, 5, 8, 10]))  # 4
    print(init.hIndex(citations=[]))  # 0
    print(init.hIndex(citations=[0]))  # 0
