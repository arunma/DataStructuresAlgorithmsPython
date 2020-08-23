from typing import List


class InsertInterval:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        merge=newInterval
        for i, curr_interval in enumerate(intervals):
            currstart, currend=curr_interval
            if currend<merge[0]:
                result.append(curr_interval)
            elif currstart>merge[1]:
                result.append(merge)
                return result+intervals[i:]
            else:
                merge[0]=min(currstart, merge[0])
                merge[1]=max(currend, merge[1])
        result.append(merge)
        return result




if __name__ == '__main__':
    init = InsertInterval()
    print(init.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))  # Output: [[1,5],[6,9]]
    print(init.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # Output: [[1,2],[3,10],[12,16]])
