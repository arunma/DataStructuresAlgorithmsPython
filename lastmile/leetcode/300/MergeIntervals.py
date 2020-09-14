from typing import List


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda each:each[0])
        result=[]
        prev=intervals[0]
        for curr in intervals[1:]:
            if prev[1]<curr[0]:
                result.append(prev)
                prev=curr
            else:
                prev[0]=min(prev[0], curr[0])
                prev[1]=max(prev[1], curr[1])

        result.append(prev)
        return result




if __name__ == '__main__':
    init = MergeIntervals()
    print(init.merge([[1,3],[2,6],[8,10],[15,18]])) #[[1,6],[8,10],[15,18]]
    print(init.merge([[1,4],[4,5]])) # [[1,5]]

