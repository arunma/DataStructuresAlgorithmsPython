class Knapsack:
    def solve_knapsack(self, profits, weights, capacity):
        R = len(profits)
        C = capacity
        dp = [[0] * (C + 1) for _ in range(R)]

        for c in range(C):
            if weights[0] <= c:
                dp[0][c] = profits[0]

        for r in range(1, R):
            for c in range(1, C + 1):
                with_curr = 0
                if weights[r] <= c:
                    with_curr = profits[r] + dp[r-1][c - weights[r]]
                without = dp[r - 1][c]
                dp[r][c] = max(with_curr, without)
        return dp[-1][-1]


if __name__ == '__main__':
    init = Knapsack()
    print(init.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(init.solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
