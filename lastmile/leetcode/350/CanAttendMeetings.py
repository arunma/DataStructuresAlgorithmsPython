from typing import List


class CanAttendMeetings:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda each: each[0])

        for i in range(1, len(intervals)):
            if not intervals[i][0] >= intervals[i - 1][1]:
                return False
        return True


if __name__ == '__main__':
    init = CanAttendMeetings()
    print(init.canAttendMeetings([[7,10],[2,4]])) #True
    print(init.canAttendMeetings([[0,30],[5,10],[15,20]])) #False
    print(init.canAttendMeetings([[5,8],[6,8]])) #False
