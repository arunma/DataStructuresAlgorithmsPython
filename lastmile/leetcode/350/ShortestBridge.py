from typing import List


class ShortestBridge:
    def shortestBridge(self, A: List[List[int]]) -> int:

        queue = []
        R = len(A)
        C = len(A[0])

        startR = -1
        startC = -1
        for r in range(R):
            for c in range(C):
                if A[r][c] == 1:
                    startR, startC = r, c
                    break

        self.findAllPartsOfIsland(A, R, C, queue, startR, startC)

        return self.findShortestBridge(A, R, C, queue)

    def findShortestBridge(self, A, R, C, queue):
        seen = set()
        while queue:
            r, c, level = queue.pop(0)
            if (r, c) not in seen:
                seen.add((r, c))
                if A[r][c] == 1:
                    return level - 1
                else:
                    npairs = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
                    for nr, nc in npairs:
                        if -1 < nr < R and -1 < nc < C and (nr, nc) not in seen:
                            queue.append((nr, nc, level + 1))
        return -1

    def findAllPartsOfIsland(self, A, R, C, queue,  r, c):

        queue.append((r, c, 0))
        A[r][c] = 0

        npairs = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in npairs:
            if -1 < nr < R and -1 < nc < C and A[nr][nc] == 1:
                self.findAllPartsOfIsland(A, R, C, queue, nr, nc)


if __name__ == '__main__':
    init = ShortestBridge()
    print(init.shortestBridge(A = [[0,1],[1,0]]))
    print(init.shortestBridge(A = [[0,1,0],[0,0,0],[0,0,1]]))
    print(init.shortestBridge(A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
