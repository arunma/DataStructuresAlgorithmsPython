from typing import List


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda each: each[0])

        mstart, mend=intervals[0]
        result=[]
        for i, interval in enumerate(intervals):
            cstart, cend=interval

            if mend>=cstart:
                mstart=min(cstart, mstart)
                mend=max(cend, mend)
            elif mend<cstart:
                result.append([mstart, mend])
                mstart,mend=interval
        result.append([mstart, mend])
        return result

if __name__ == '__main__':
    init = MergeIntervals()
    print(init.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
    print(init.merge(intervals = [[1,4],[4,5]]))
