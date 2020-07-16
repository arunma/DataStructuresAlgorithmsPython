from typing import List


class Triangle:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return -1
        n = len(triangle)
        dp = [0] * (n+1)
        for r in range(n - 1, -1, -1):
            for c in range(len(triangle[r])):
                dp[c] = min(dp[c], dp[c + 1]) + triangle[r][c]
        return dp[0]


if __name__ == '__main__':
    init = Triangle()
    print(init.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))  # 11
