from math import sqrt


class PerfectSquares:
    def numSquares(self, n: int) -> int:
        square_nums = []
        for i in range(0, int(sqrt(n)) + 1):
            square_nums.append(i * i)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for sq in square_nums:
                if i < sq: #Optimization
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[-1]


if __name__ == '__main__':
    init = PerfectSquares()
    print(init.numSquares(12))  # 3
    print(init.numSquares(13))  # 2
    print(init.numSquares(1))  # 1
    print(init.numSquares(2))  # 2
    print(init.numSquares(3))  # 3
