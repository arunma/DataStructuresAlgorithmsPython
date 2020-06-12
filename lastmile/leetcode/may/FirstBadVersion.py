class FirstBadVersion:
    def __init__(self, n):
        self.target = n

    def isBadVersion(self, n) -> bool:
        if (n >= self.target):
            return True
        else:
            return False

    def firstBadVersion(self, n) -> int:
        low = 1
        high = n

        while low < high:
            mid = low + (high - low) // 2
            if self.isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        if self.isBadVersion(low):
            return low
        return high


if __name__ == '__main__':
    first = FirstBadVersion(4)
    print(first.firstBadVersion(7))

    second = FirstBadVersion(2147483647)
    print(second.firstBadVersion(2147483647))

    third = FirstBadVersion(5)
    print(third.firstBadVersion(4))
