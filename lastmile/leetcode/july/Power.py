class Power:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x

        result = 1

        while n:
            if n & 1:
                result = result * x

            x = x * x
            n = n // 2

        return result


if __name__ == '__main__':
    init = Power()
    print(init.myPow(2.00000, 10))
    print(init.myPow(2.10000, 3))
    print(init.myPow(2.00000, -2))
