def count_subsets(nums, sum):
    C = sum + 1
    R = len(nums)
    dp = [[0] * C for _ in range(R)]
    for r in range(R):
        dp[r][0] = 1

    for c in range(C):
        if nums[0] == c:
            dp[0][c] = 1

    for r in range(1, R):
        for c in range(1, C):
            dp[r][c] = dp[r - 1][c]
            if c >= nums[r]:
                dp[r][c] += dp[r - 1][c - nums[r]]
    return dp[-1][-1]


if __name__ == '__main__':
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))  # 3
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))  # 3
