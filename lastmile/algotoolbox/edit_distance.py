# Uses python3
def edit_distance(s, t):
    n1 = len(s)
    n2 = len(t)
    dp = [[0] * (n2+1) for _ in range(n1 + 1)]

    for r in range(1, n1 + 1):
        dp[r][0] = r
    for c in range(1, n2 + 1):
        dp[0][c] = c

    for r in range(1, n1 + 1):
        for c in range(1, n2 + 1):
            if s[r - 1] == t[c - 1]:
                dp[r][c] = dp[r - 1][c - 1]
            else:
                dp[r][c] = min(dp[r - 1][c - 1], dp[r][c - 1], dp[r - 1][c]) + 1

    return dp[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    #print(edit_distance("short", "ports")) #3
