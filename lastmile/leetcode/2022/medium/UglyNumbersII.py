import heapq


class UglyNumbers:
    def nthUglyNumber(self, n: int) -> int:
        if n==1:
            return 1
        dp=[0]*(n+1)
        dp[1]=1

        i2=i3=i5=1

        for i in range(2,n+1):
            min_next=min(dp[i2]*2, dp[i3]*3, dp[i5]*5)
            dp[i]=min_next

            if dp[i]==dp[i2]*2:
                i2+=1
            if dp[i]==dp[i3]*3:
                i3+=1
            if dp[i]==dp[i5]*5:
                i5+=1

        return dp[-1]









if __name__ == '__main__':
    init = UglyNumbers()
    print(init.nthUglyNumber(10)) #12
    print(init.nthUglyNumber(11)) #15
    print(init.nthUglyNumber(1))  #1
