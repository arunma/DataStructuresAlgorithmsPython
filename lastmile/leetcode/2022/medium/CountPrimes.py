class CountPrimes:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        dp = [True] * (n)
        dp[0] = dp[1] = False
        ans=0
        for i in range(2, n):
            if dp[i]:
                for x in range(i * i, n, i):
                    dp[x] = False
                ans+= 1

        return ans


if __name__ == "__main__":
    init = CountPrimes()
    print(init.countPrimes(3))  # 1
    print(init.countPrimes(10))  # 4
    print(init.countPrimes(20))  # 8
    print(init.countPrimes(0))  # 0
    print(init.countPrimes(1))  # 0
