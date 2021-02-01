from typing import List


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=lambda x:x[0])
        mstart, mend=intervals[0]
        result=[]

        for cinterval in intervals:
            cstart,cend=cinterval

            if mend>=cstart:
                mstart=min(cstart, mstart)
                mend=max(cend, mend)
            else:
                result.append([mstart, mend])
                mstart,mend=cinterval

        result.append([mstart,mend])

        return result

if __name__ == '__main__':
    init = MergeIntervals()
    print(init.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
    print(init.merge(intervals = [[1,4],[4,5]]))
