from collections import deque
import heapq
from typing import List


class MazeII:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        R = len(maze)
        C = len(maze[0])

        pq = [(0, start[0], start[1])]
        destr, destc = destination[0], destination[1]
        visited=set()

        while pq:
            dist, r, c = heapq.heappop(pq)
            if (r,c) in visited:
                continue

            visited.add((r,c))
            if destr == r and destc == c:
                return dist

            dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in dir:
                nr,nc,ndist=r,c,dist
                while -1<nr+dr<R and -1<nc+dc<C and maze[nr+dr][nc+dc]==0:
                    nr+=dr
                    nc+=dc
                    ndist+=1
                heapq.heappush(pq, (ndist,nr,nc))
        return -1



if __name__ == '__main__':
    init = MazeII()
    print(init.shortestDistance(
        maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4],
        destination=[4, 4]))
