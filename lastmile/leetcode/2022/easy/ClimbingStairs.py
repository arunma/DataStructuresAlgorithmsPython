class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        dp = {1:1, 2:2}
        self.climbStairsInner(n, dp)
        return dp[n]

    def climbStairsInner(self, n, dp):
        if n in dp:
            return dp[n]
        else:
            dp[n] = self.climbStairsInner(n-1, dp) + self.climbStairsInner(n-2, dp)
            return dp[n]


if __name__ == "__main__":
    init = ClimbingStairs()
    print(init.climbStairs(2))  # 2
    print(init.climbStairs(3))  # 3
    print(init.climbStairs(5))  # 8
