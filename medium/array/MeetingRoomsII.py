import heapq
from typing import List


class MeetingRoomsII:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k:k[0])
        pq=[]

        for s,e in intervals:
            if pq and s>=pq[0]:
                heapq.heappushpop(pq, e)
            else:
                heapq.heappush(pq, e)
        return len(pq)


if __name__ == "__main__":
    init = MeetingRoomsII()
    print(init.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(init.minMeetingRooms([[7, 10], [2, 4]]))
