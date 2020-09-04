class PowXN:
    def myPow(self, x, n):
        if n<0:
            x=1/x
            n=-n
        result=1
        while n:
            result*=x
            n=n-1
        return result


# def myPow(self, x: float, n: int) -> float:
    #     if n < 0:
    #         x = 1 / x
    #         n = -n
    #
    #     # result=1
    #     # while n > 0:
    #     #     result = result * x
    #     #     n = n-1
    #     # return result
    #     result = 1
    #     while n:
    #         print("{},{},{}", n, x, result)
    #         if n % 2 == 1:
    #             result = result * x
    #         x = x * x
    #         n = n // 2
    #     return result


if __name__ == '__main__':
    init = PowXN()
    print(init.myPow(2.00000, 10))  # 1024.00000
    print(init.myPow(2.10000, 3))  # 9.26100
    print(init.myPow(2.00000, -2))  # 0.25
