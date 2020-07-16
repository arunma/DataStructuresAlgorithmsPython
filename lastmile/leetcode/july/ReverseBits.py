class ReverseBits:
    def reverseBits(self, n: int) -> int:
        print (bin(0x00ff00ff))
        print (bin(0x0f0f0f0f))
        print (bin(0x33333333))
        print (bin(0x55555555))
        result = 0
        for i in range(32):
            band = n & 1
            result <<= 1
            result |= band
            n >>= 1
        return result


if __name__ == '__main__':
    init = ReverseBits()
    print(init.reverseBits(0b00000010100101000001111010011100))
