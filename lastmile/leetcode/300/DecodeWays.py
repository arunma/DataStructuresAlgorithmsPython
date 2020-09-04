class DecodeWays:
    #Without Memo
    def numDecodings(self, s: str) -> int:
        return self.numDecodingsInner(s, 0)

    def numDecodingsInner(self, s, index):
        # Ideally, we should be able to do this if not for the '0' condition that's required
        if index == len(s):  # or index==len[s]-1:
            return 1
        if s[index] == '0':
            return 0
        if index == len(s) - 1:
            return 1

        ans = self.numDecodingsInner(s, index + 1)
        if int(s[index:index + 2]) <= 26:
            ans += self.numDecodingsInner(s, index + 2)

        return ans

    #With memo
    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.numDecodingsInner(s, 0, memo)

    def numDecodingsInner(self, s, index, memo):
        # Ideally, we should be able to do this if not for the '0' condition that's required
        if index == len(s):  # or index==len[s]-1:
            return 1
        if s[index] == '0':
            return 0
        if index == len(s) - 1:
            return 1

        if index in memo:
            return memo[index]

        ans = self.numDecodingsInner(s, index + 1, memo)
        if int(s[index:index + 2]) <= 26:
            ans += self.numDecodingsInner(s, index + 2, memo)
        memo[index] = ans

        return memo[index]


if __name__ == '__main__':
    init = DecodeWays()
    print(init.numDecodings("12"))  # 2
    print(init.numDecodings("226"))  # 3
    print(init.numDecodings("132226"))  # 3
