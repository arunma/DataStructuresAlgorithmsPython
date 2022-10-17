from typing import List


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda k: k[0])

        start, end = intervals[0]
        result = []

        for s, e in intervals[1:]:
            if s <= end:
                start = min(start, s)
                end = max(end, e)
            else:
                result.append([start, end])
                start, end = s, e

        result.append([start, end])
        return result

if __name__ == "__main__":
    init = MergeIntervals()
    print(init.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])) # [[1,6],[8,10],[15,18]]
    print(init.merge(intervals=[[1, 4], [4, 5]])) # [[1,5]]
