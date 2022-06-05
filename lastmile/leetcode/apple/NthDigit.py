class NthDigit:
    def findNthDigit(self, n: int) -> int:
        count=9
        len=1
        start=1

        while n>(count*len):
            n-=count*len
            count*=10
            len+=1
            start*=10

        number = start + (n-1)/len
        position=(n-1)%len
        res = str(number)[position]
        return res


if __name__ == '__main__':
    init = NthDigit()
    print(init.findNthDigit(11))
    print(init.findNthDigit(1000))
