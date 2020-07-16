def can_partition(nums):
    R = len(nums)
    total = sum(nums)
    target = total // 2

    if total != target * 2:
        return False

    C = target
    dp = [[0] * (C + 1) for _ in range(R)]

    for c in range(C + 1):
        if nums[0] <= c:
            dp[0][c] = nums[0]

    for r in range(1, R):
        for c in range(1, C + 1):
            with_curr = 0
            if nums[r] <= c:
                with_curr = nums[r] + dp[r - 1][c - nums[r]]
            without_curr = dp[r - 1][c]
            dp[r][c] = max(with_curr, without_curr)
            if dp[r][c] == target:
                return True
    return False


def can_partition_two(nums):
    R = len(nums)
    total = sum(nums)
    target = total // 2

    if total != target * 2:
        return False

    C = target + 1
    dp = [[False] * C for _ in range(R)]

    for c in range(C):
        if nums[0] == c:
            dp[0][c] = True
    dp[0][0] = True

    for r in range(1, R):
        for c in range(1, C):
            if dp[r - 1][c]:
                dp[r][c] = True
            else:
                dp[r][c] = dp[r - 1][c - nums[r]]
    # for r in range(1, R):
    #     for c in range(1, C):
    #         without = dp[r - 1][c]
    #         with_c = False
    #         if c >= nums[r]:
    #             with_c = dp[r - 1][c - nums[r]]
    #         dp[r][c]=without or with_c
    return dp[-1][-1]


if __name__ == '__main__':
    print("Can partition: " + str(can_partition_two([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition_two([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition_two([2, 3, 4, 6])))
