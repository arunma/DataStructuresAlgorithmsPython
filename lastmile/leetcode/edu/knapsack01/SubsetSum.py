def can_partition(nums, sum):
    C = sum + 1
    R = len(nums)

    dp = [[0] * C for _ in range(R)]
    for c in range(C):
        if nums[0] <= c:
            dp[0][c] = nums[0]

    for r in range(1, R):
        for c in range(1, C):
            with_curr = 0
            if nums[r] <= c:
                with_curr = nums[r] + dp[r - 1][c - nums[r]]
            without_curr = dp[r - 1][c]
            dp[r][c] = max(with_curr, without_curr)
            if dp[r][c] == sum:
                return True
    return False


if __name__ == '__main__':
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))  # True
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))  # True
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))  # False
