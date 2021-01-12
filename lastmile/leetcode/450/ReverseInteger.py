class ReverseInteger:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        sx=str(x)
        sign=1
        if sx[0]=='-':
            sx=sx[1:]
            sign=-1

        result=int(sx[::-1])
        intMax=2**31

        if -intMax-1<result<intMax:
            return sign*result
        return 0


if __name__ == '__main__':
    init = ReverseInteger()
    print(init.reverse(1534236469))
    print(init.reverse(-123))
