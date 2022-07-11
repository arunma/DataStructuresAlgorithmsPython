import math

class CountNumberOfWaysToPlaceHouses:
    def countHousePlacementsInner(self, n: int) -> int:
        dp = [0]* (n + 1)
        if n==1:
            return 2
        elif n==2:
            return 3
        dp[1] = 2
        dp[2] = 3

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def countHousePlacements(self, n: int) -> int:
        mod = 1_000_000_007
        res=self.countHousePlacementsInner(n)%mod
        res=pow(res, 2) % mod
        return res

if __name__ == '__main__':
    init = CountNumberOfWaysToPlaceHouses()
    print(init.countHousePlacements(1)) #4
    print(init.countHousePlacements(2)) #9
    print(init.countHousePlacements(3)) #25
    print(init.countHousePlacements(5)) #169
