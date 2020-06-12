# Uses python3
import sys
import math


def get_change(money):
    dp = [sys.maxsize] * (money + 1)
    dp[0] = 0
    for m in range(1, money + 1):
        for c in [1, 3, 4]:
            if m >= c:
                dp[m] = min(dp[m], 1 + dp[m - c])
    return dp[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    #print(get_change(2)) #2
    #print(get_change(34)) #9
