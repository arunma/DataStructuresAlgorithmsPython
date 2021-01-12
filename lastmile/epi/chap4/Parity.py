class Parity:
    def parity1(self, x):
        result = 0
        while x:
            result ^= (x & 1)
            x >>= 1
        return result

    def parity2(self, x):
        result = 0
        while x:
            result ^= 1
            x = x & (x - 1)
        return result


if __name__ == '__main__':
    init = Parity()
    print(str(bin(41)))
    print(init.parity2(41))
2
3
10
24679
