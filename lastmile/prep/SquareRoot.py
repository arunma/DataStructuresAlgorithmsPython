class SquareRoot:
    def mySqrt(self, x: int) -> int:
        # r = x
        # while r * r > x:
        #     r = (r + x / r) / 2
        # return r
        left=2
        right=x//2
        while left<=right:
            mid=left+(right-left)//2
            num=mid*mid
            if num==x:
                return mid
            elif num>x:
                right=mid-1
            else:
                left=mid+1
        return right


if __name__ == '__main__':
    init = SquareRoot()
    print(init.mySqrt(4))
    print(init.mySqrt(8))
