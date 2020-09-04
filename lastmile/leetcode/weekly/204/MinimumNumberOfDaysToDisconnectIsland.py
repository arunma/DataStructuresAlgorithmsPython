from collections import defaultdict
from typing import List


class MinimumNumberOfDaysToDisconnectIsland:
    # def minDays(self, grid: List[List[int]]) -> int:
    #
    #     def dfs(grid, r, c, colors, R, C):
    #         colors[(r, c)] = GRAY
    #         if -1 < r < R and -1 < c < C and grid[r][c]==1:
    #             grid[r][c]=0
    #             npairs=[(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    #             for nrow, ncol in npairs:
    #                 if colors[(nrow, ncol)]==WHITE:
    #                     dfs(grid, nrow, ncol, colors, R, C)
    #
    #         colors[(r,c)]=BLACK
    #
    #
    #     queue=[]
    #     R = len(grid)
    #     C=len(grid[0])
    #
    #     days=0
    #
    #     WHITE, GRAY, BLACK=0,1,2
    #     colors=defaultdict(int)
    #
    #     for r in range(R):
    #         for c in range(C):
    #             if grid[r][c]==1:
    #                 if colors[(r,c)]==WHITE:
    #                     dfs(grid, r,c, colors, R, C)
    #                     days += 1
    #     return days

    # def minDays(self, grid: List[List[int]]) -> int:
    #
    #     queue=[]
    #     R = len(grid)
    #     C=len(grid[0])
    #
    #     days=0
    #
    #     visited=[[False] *C for _ in range(R)]
    #
    #     for r in range(R):
    #         for c in range(C):
    #             if grid[r][c]==1:
    #                 queue.append((r,c))
    #
    #     while queue:
    #         crow, ccol=queue.pop(0)
    #         if not visited[crow][ccol]:
    #             days += 1
    #         visited[crow][ccol]=True
    #
    #         npairs = [(crow - 1, ccol), (crow + 1, ccol), (crow, ccol - 1), (crow, ccol + 1)]
    #         for nrow, ncol in npairs:
    #             if -1<nrow<R and -1<ncol<C and grid[nrow][ncol]==1:
    #                 queue.append((nrow, ncol))
    #
    #     return days

    def minDays(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])

        def check_connected(grid):
            n_nodes = 0
            for i in range(self.m):
                for j in range(self.n):
                    if grid[i][j] == 1:
                        n_nodes += 1
                        xs, ys = i, j
            if n_nodes == 0:
                return True
            to_visit = [[xs, ys]]
            visited = set([(xs, ys)])
            while len(to_visit) > 0:
                nx, ny = to_visit.pop(0)
                nexts = [[nx + 1, ny], [nx - 1, ny], [nx, ny + 1], [nx, ny - 1]]
                nexts = [[i, j] for i, j in nexts if all([0 <= i < self.m, 0 <= j < self.n])]
                for ni, nj in nexts:
                    if grid[ni][nj] == 0:
                        continue
                    if (ni, nj) in visited:
                        continue
                    visited.add((ni, nj))
                    to_visit.append([ni, nj])
            # print(visited)
            # print(len(visited), n_nodes)
            if len(visited) == n_nodes:
                return False
            return True

        if check_connected(grid):
            return 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if check_connected(grid):
                        return 1
                    grid[i][j] = 1
        return 2




if __name__ == '__main__':
    init = MinimumNumberOfDaysToDisconnectIsland()
    print(init.minDays(grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]])) #2
    print(init.minDays(grid = [[1,1]])) #2
    print(init.minDays(grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]])) #1

