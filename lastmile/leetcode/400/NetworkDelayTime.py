import sys
from typing import List

#https://leetcode.com/problems/network-delay-time/
#All nodes shortest path - Floyd Warshall

class NetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        distances=[[sys.maxsize] * N for _ in range(N)]

        for u,v, w in times:
            distances[u-1][v-1]=w

        for i in range(N):
            distances[i][i]=0

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    distances[i][j]=min(distances[i][j], distances[i][k]+ distances[k][j])

        result=max(distances[K-1])
        return -1 if result==sys.maxsize else result


if __name__ == '__main__':
    init = NetworkDelayTime()
    print(init.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2)) #2
