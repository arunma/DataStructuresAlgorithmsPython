class CountBits:
    def countBits(self, x):
        count = 0
        while x:
            count += (x & 1)
            x >>= 1
        return count


if __name__ == '__main__':
    init = CountBits()
    print(init.countBits(11))
