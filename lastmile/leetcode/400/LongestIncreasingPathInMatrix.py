from typing import List


class LongestIncreasingPathInMatrix:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        R = len(matrix)
        C = len(matrix[0])

        dp = [[0] * C for _ in range(R)]

        maxResult = 0
        for r in range(R):
            for c in range(C):
                maxResult = max(maxResult, self.dfs(matrix, dp, R, C, r, c))

        return maxResult

    def dfs(self, matrix, dp, R, C, r, c):
        if dp[r][c] == 0:
            npairs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            currMax = 1
            for nr, nc in npairs:
                if -1 < nr < R and -1 < nc < C and matrix[nr][nc] > matrix[r][c]:
                    currMax = max(currMax, 1 + self.dfs(matrix, dp, R, C, nr, nc))

            dp[r][c] = currMax
        return dp[r][c]


if __name__ == '__main__':
    init = LongestIncreasingPathInMatrix()
    print(init.longestIncreasingPath(
        [
            [9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]
        ]))  # 4

    print(init.longestIncreasingPath(
        [
            [3, 4, 5],
            [3, 2, 6],
            [2, 2, 1]
        ]))  # 4
