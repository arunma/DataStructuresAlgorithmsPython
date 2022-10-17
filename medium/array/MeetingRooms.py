from typing import List


class MeetingRooms:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda k: k[0])
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if s < end:
                return False
            else:
                start, end = s, e
        return True


if __name__ == "__main__":
    init = MeetingRooms()
    print(init.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))  # False
    print(init.canAttendMeetings([[7, 10], [2, 4]]))  # True
