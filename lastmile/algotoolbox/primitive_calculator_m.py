# Uses python3
import sys


# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)
def optimal_sequence(num):
    dp = [0] * (num + 1)
    for n in range(2, num + 1):
        min1 = dp[n - 1]
        min2 = sys.maxsize
        min3 = sys.maxsize
        if n % 2 == 0:
            min2 = dp[int(n / 2)]
        if n % 3 == 0:
            min3 = dp[int(n / 3)]

        minOp = min(min1, min2, min3) + 1
        dp[n] = minOp

    return dp[-1]




# input = sys.stdin.read()
# n = int(input)
n = 96234
dp = optimal_sequence(n)
print(dp)
