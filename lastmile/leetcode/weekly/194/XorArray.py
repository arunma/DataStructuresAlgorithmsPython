class XorArray:
    def xorOperation(self, n: int, start: int) -> int:
        xor = start
        for i in range(1, n):
            next = start + (2 * i)
            xor = xor ^ next
        return xor


if __name__ == '__main__':
    init = XorArray()
    print(init.xorOperation(5, 0))  # 8
    print(init.xorOperation(4, 3))  # 8
    print(init.xorOperation(10, 5))  # 2
