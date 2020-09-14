from typing import List


class InsertInterval:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        mstart, mend=newInterval
        result=[]
        for i, curr in enumerate(intervals):
            cstart, cend=curr
            if cend<mstart:
                result.append(curr)
            elif cstart>mend:
                result.append([mstart,mend])
                return result+intervals[i:]
            else:
                mstart=min(cstart, mstart)
                mend=max(cend, mend)
        result.append([mstart, mend])
        return result



if __name__ == '__main__':
    init = InsertInterval()
    print(init.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])) #[[1,5],[6,9]]
    print(init.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])) #[[1,2],[3,10],[12,16]]
