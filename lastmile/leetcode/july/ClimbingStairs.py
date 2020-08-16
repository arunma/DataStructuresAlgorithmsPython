class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for s in range(3, n+1):
            dp[s] = dp[s - 1] + dp[s - 2]

        return dp[-1]


if __name__ == '__main__':
    init = ClimbingStairs()
    print(init.climbStairs(2))  # 2
    print(init.climbStairs(3))  # 3
    print(init.climbStairs(5))  # 8
