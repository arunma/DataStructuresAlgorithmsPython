def can_partition(nums):
    C = (sum(nums) // 2) + 1
    R = len(nums)
    dp = [[False] * C for _ in range(R)]
    for r in range(R):
        dp[r][0] = True

    for c in range(C):
        if c == nums[0]:
            dp[0][c] = True

    for r in range(1, R):
        for c in range(1, C):
            if dp[r - 1][c]:
                dp[r][c] = dp[r - 1][c]
            elif c>=nums[r]:
                dp[r][c] = dp[r-1][c-nums[r]]

    column=0
    for c in range(C):
        if dp[-1][c]:
            column=c

    first_value=column
    second_value=sum(nums)-first_value
    return second_value-first_value




if __name__ == '__main__':
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))  # 3
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))  # 0
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))  # 92
