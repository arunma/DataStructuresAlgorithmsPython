from collections import defaultdict


def numberOfWays(arr, k):
    seen = defaultdict(int)
    count = 0
    for num in arr:
        remain = k - num
        if remain in seen:
            count += seen[remain]
        seen[num] += 1
    return count


if __name__ == '__main__':
    print(numberOfWays([1, 2, 3, 4, 3], 6))  # 2
    print(numberOfWays([1, 5, 3, 3, 3], 6))  # 4
