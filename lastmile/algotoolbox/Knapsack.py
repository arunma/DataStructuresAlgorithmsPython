# Uses python3
import sys


# def optimal_weight(W, weights):
#     # write your code here
#     dp = [[0] * (W + 1) for _ in range((len(weights) + 1))]
#
#     for r in range(1, (len(weights) + 1)):
#         for c in range(1, W + 1):
#             with_curr = 0
#             without_curr = 0
#             if w[r - 1] <= c:
#                 with_curr = w[r - 1] + dp[r - 1][c - w[r - 1]]
#             else:
#                 without_curr = dp[r - 1][c]
#             dp[r][c] = max(with_curr, without_curr)
#     return dp[-1][-1]


def optimal_weight(W, weights):
    C = W + 1
    R = len(weights) + 1

    dp = [[0] * C for _ in range(R)]
    for r in range(1, R):
        for c in range(1, C):
            without_c = dp[r - 1][c]
            with_c = 0
            if weights[r - 1] <= c:
                with_c = weights[r - 1] + dp[r - 1][c - weights[r - 1]]
            dp[r][c] = max(with_c, without_c)
    return dp[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

# if __name__ == '__main__':
#     W = 10
#     w = [1, 4, 8]
#     print(optimal_weight(W, w))  # 9
