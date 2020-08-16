class PowerOf4:
    # def isPowerOfFour(self, num: int) -> bool:
    #     while num % 4 == 0:
    #         num = num / 4
    #     return num == 1

    def isPowerOfFour(self, num: int) -> bool:
        if (num > 0) and (num & (num - 1) == 0) and (num & 0xaaaaaaaa == 0):
            return True
        return False


if __name__ == '__main__':
    init = PowerOf4()
    print(init.isPowerOfFour(16))  # true
    print(init.isPowerOfFour(5))  # false
