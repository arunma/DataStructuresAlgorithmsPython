import sys
from typing import List


class MinimumTimeToCompleteAllTrips:
    # def minimumTime(self, times: List[int], totalTrips: int) -> int:
    #     if totalTrips==1:
    #         return min(times)
    #     maxTrips=min(times) * totalTrips
    #     dp=[0] * (maxTrips+1)
    #     times.sort()
    #     for time in times:
    #         for index,trip in enumerate(range(1,maxTrips+1)):
    #             if time<=trip:
    #                 dp[trip]=max(dp[trip], dp[trip-time])+1
    #
    #
    #     if dp[trip]==totalTrips:
    #         return index-1
    #     return 0

    def minimumTime(self, times: List[int], totalTrips: int) -> int:
        maxTrips=min(times)*totalTrips
        low=0
        high=maxTrips

        def tripsHigh(mid):
            totalTripsAtMid=0
            for time in times:
                totalTripsAtMid+=mid//time
            return totalTripsAtMid>=totalTrips

        while low<=high:
            mid=low+(high-low)//2
            if tripsHigh(mid):
                high=mid-1
            else:
                low=mid+1
        return low




if __name__ == '__main__':
    init = MinimumTimeToCompleteAllTrips()
    #print(init.minimumTime(times = [1,2,3], totalTrips = 5)) #3
    #print(init.minimumTime(times = [2], totalTrips = 1)) #2
    print(init.minimumTime(times = [5,10,10], totalTrips = 9)) #25