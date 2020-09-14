class StairCaseUniqueWays:
    def uniqueWays(self, N):
        dp = [0] * (N + 1)
        dp[0] = 1
        for i in range(1, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    init = StairCaseUniqueWays()
    print(init.uniqueWays(4))  # 5
