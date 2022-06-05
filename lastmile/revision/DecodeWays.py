class DecodeWays:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        N = len(s)
        dp = [0] * (N + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, N + 1):
            if 0 < int(s[i - 1:i]) < 10:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    init = DecodeWays()
    print(init.numDecodings("12"))  # 2
    print(init.numDecodings("226"))  # 3
    print(init.numDecodings("132226"))  # 10
