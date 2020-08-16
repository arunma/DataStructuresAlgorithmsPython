class SquareRoot:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                r = mid
            else:
                l = mid + 1


if __name__ == '__main__':
    init = SquareRoot()
    print(init.mySqrt(4))
    print(init.mySqrt(8))
