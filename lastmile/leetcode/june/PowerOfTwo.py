import math


class PowerOfTwo:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return math.log2(n).is_integer()


if __name__ == '__main__':
    init = PowerOfTwo()
    print(init.isPowerOfTwo(1))  # true
    print(init.isPowerOfTwo(16))  # true
    print(init.isPowerOfTwo(218))  # false
    print(init.isPowerOfTwo(0))  # false
    print(init.isPowerOfTwo(-16))  # false
