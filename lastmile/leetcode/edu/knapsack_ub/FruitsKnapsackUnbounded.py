def solve_knapsack(profits, weights, capacity):
    C = capacity + 1
    R = len(profits)

    dp = [[0] * C for _ in range(R)]
    for c in range(C):
        if c >= weights[0]:
            dp[0][c] = profits[0] + dp[0][c - weights[0]]

    for r in range(1, R):
        for c in range(1, C):
            _without = dp[r-1][c]
            _with=0
            if c>=weights[r]:
                _with=profits[r]+dp[r-1][c-weights[r]]
            dp[r][c]=max(_with, _without)
    return dp[-1][-1]


if __name__ == '__main__':
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))  # 140
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))  # 105
