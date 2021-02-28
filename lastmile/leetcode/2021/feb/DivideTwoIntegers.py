import sys


class DivideTwoIntegers:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        positive = (dividend < 0) == (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            curr = 0
            while dividend >= divisor << (curr + 1):
                curr += 1
            result += 1 << curr
            dividend -= divisor << curr
        return min(result if positive else -result, sys.maxsize)


if __name__ == '__main__':
    init = DivideTwoIntegers()
    print(init.divide(7, -3))  # -2
    print(init.divide(0, 1))  # 0
    print(init.divide(1, 1))  # 1
