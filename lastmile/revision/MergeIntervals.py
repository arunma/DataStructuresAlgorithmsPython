from typing import List


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]

        intervals.sort(key=lambda x: x[0])
        mstart,mend=intervals[0]

        for cstart, cend in intervals:
            if mend>=cstart:
                mstart=min(mstart, cstart)
                mend=max(mend, cend)
            else:
                result.append([mstart,mend])
                mstart,mend=cstart,cend

        result.append([mstart,mend])
        return result




if __name__ == '__main__':
    init = MergeIntervals()
    print(init.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])) #[[1,6],[8,10],[15,18]]
    print(init.merge(intervals=[[1, 4], [4, 5]])) #[[1,5]]
