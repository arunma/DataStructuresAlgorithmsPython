import sys


def can_partition(nums):
    total = sum(nums)
    target = (total // 2)
    R = len(nums)
    C = target + 1
    dp = [[False] * C for _ in range(R)]

    dp[0][0] = True
    for c in range(C):
        if nums[0] == c:
            dp[0][c] = True

    for r in range(1, R):
        for c in range(1, C):
            if dp[r - 1][c]:
                dp[r][c] = True
            elif nums[r] <= c:
                dp[r][c] = dp[r - 1][c - nums[r]]

    # checking last column of last row that has been set to true
    col = -1
    for c in range(C):
        if dp[-1][c]:
            col = c

    first_partition = col
    second_partition = total - first_partition

    return abs(first_partition - second_partition)


if __name__ == '__main__':
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))  # 3
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))  # 0
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))  # 92
