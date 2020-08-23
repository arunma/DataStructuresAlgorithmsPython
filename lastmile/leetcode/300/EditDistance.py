class EditDistance:

    def minDistance(self, word1, word2):
        R = len(word1)
        C = len(word2)

        if not word1:
            return C
        if not word2:
            return R

        dp = [[0] * (C + 1) for _ in range(R + 1)]

        for r in range(R + 1):
            dp[r][0] = r
        for c in range(C + 1):
            dp[0][c] = c

        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    init = EditDistance()
    print(init.minDistance(word1="horse", word2="ros"))  # 3
    print(init.minDistance(word1="intention", word2="execution"))  # 5
    print(init.minDistance(word1="a", word2="b"))  # 1
