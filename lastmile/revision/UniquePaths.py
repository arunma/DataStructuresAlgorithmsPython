class UniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    init = UniquePaths()
    print(init.uniquePaths(3, 2))  # 3
    print(init.uniquePaths(7, 3))  # 28
