from typing import List


class NonOverlappingIntervals:
    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     intervals.sort()
    #     prevEnd=intervals[0][1]
    #     result=0
    #     for start, end in intervals[1:]:
    #         if start>=prevEnd: #non overlapping
    #             prevEnd=end
    #         else:
    #             result+=1
    #     return result

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k: k[1])

        pend = intervals[0][1]
        result = 0

        for start, end in intervals[1:]:
            if start >= pend:  # no overlap
                pend = end
            else:
                result += 1

        return result


if __name__ == '__main__':
    init = NonOverlappingIntervals()
    print(init.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))#1
    print(init.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]])) #2
    print(init.eraseOverlapIntervals(intervals = [[1,2],[2,3]])) #0
