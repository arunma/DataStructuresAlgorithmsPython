from typing import List


class TheMaze:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        R = len(maze)
        C = len(maze[0])
        visited = set()
        return self.dfs(maze, R, C, visited, (start[0], start[1]), (destination[0], destination[1]))

    def dfs(self, maze, R, C, visited, start, end):
        #print(start)
        if start in visited:
            return False

        visited.add(start)

        if start == end:
            return True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            sr, sc = start
            while -1 < sr+dr < R and -1 < sc+dc < C and maze[sr + dr][sc + dc] == 0:
                sr+=dr
                sc+=dc
            if self.dfs(maze, R, C, visited, (sr, sc), end):
                return True
        return False


if __name__ == '__main__':
    init = TheMaze()
    print(init.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4])) #true
    print(init.hasPath(maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2])) #false
    print(init.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4],[1, 2])) # true
