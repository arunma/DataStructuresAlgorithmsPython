from collections import defaultdict


class BFS:

    def shortestPath(self, matrix, start, end):
        R = len(matrix)
        C = len(matrix[0])

        visited = [[False] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if self.bfs(matrix, start, end, visited):
                    return True
        return False

    def bfs(self, matrix, start, end, visited):
        queue = []
        srow, scol = start
        queue.append((srow, scol))
        while queue:
            srow, scol = queue.pop(0)
            visited[srow][scol]=True
            if srow==end[0] and scol==end[1]:
                return True
            npairs = [(srow - 1, scol), (srow + 1, scol), (srow, scol - 1), (srow, scol + 1)]
            for nrow, ncol in npairs:
                if (-1<nrow<len(matrix)) and (-1<ncol<len(matrix[0])) and not visited[nrow][ncol] and matrix[nrow][ncol]=='*':
                    queue.append((nrow, ncol))
        return


if __name__ == '__main__':
    init = BFS()
    matrix = [['0', '*', '0', '*'],
              ['*', '0', '*', '*'],
              ['0', '*', '*', '*'],
              ['*', '*', '*', '*']]
    print(init.shortestPath(matrix, start=[0, 3], end=[3, 0]))  # 0,3,7
