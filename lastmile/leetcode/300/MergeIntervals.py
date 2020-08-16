from typing import List


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda each:each[0])
        result=[]
        for interval in intervals:
            if not result or result[-1][1]<interval[0]:
                result.append(interval)
            else:
                result[-1][1]=max(result[-1][1], interval[1])
        return result


if __name__ == '__main__':
    init = MergeIntervals()
    print(init.merge([[1,3],[2,6],[8,10],[15,18]])) #[[1,6],[8,10],[15,18]]
    print(init.merge([[1,4],[4,5]])) # [[1,5]]

