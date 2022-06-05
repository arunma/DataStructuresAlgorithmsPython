class ClimbStairs:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    init = ClimbStairs()
    print(init.climbStairs(2))  # 2
    print(init.climbStairs(3))  # 3
    print(init.climbStairs(5))  # 8
