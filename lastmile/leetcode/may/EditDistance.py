class EditDistance:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        if not n1:
            return n2
        elif not n2:
            return n1

        dp = [[0 for c in range(n2 + 1)] for r in range(n1 + 1)]

        for r in range(n1 + 1):
            dp[r][0] = r

        for c in range(1, n2 + 1):
            dp[0][c] = c

        for r in range(1, n1 + 1):
            for c in range(1, n2 + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = 1 + min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1])

        return dp[n1][n2]


if __name__ == '__main__':
    init = EditDistance()
    print(init.minDistance(word1="horse", word2="ros"))  # 3
    print(init.minDistance(word1="intention", word2="execution"))  # 5
    print(init.minDistance(word1="a", word2="b"))  # 1
