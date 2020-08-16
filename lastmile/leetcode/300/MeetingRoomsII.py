import sys
from typing import List
import heapq


class MeetingRoomsII:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        rooms = []
        intervals.sort(key=lambda each: each[0])
        heapq.heappush(rooms, intervals[0][1])
        min_rooms = 1

        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
            min_rooms=max(min_rooms, len(rooms))
        return min_rooms


if __name__ == '__main__':
    init = MeetingRoomsII()
    print(init.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # 2
    print(init.minMeetingRooms([[7, 10], [2, 4]]))  # 1
    print(init.minMeetingRooms([[2, 7]]))  # 1
