class Power:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1
        if n==1: return x
        if n<0: return self.myPow(1/x, -n)
        d, m = divmod(n, 2)
        # x^10 = (x^2)^5
        if m==0:
            return self.myPow(x*x, n//2)
        else:
            return x* self.myPow(x*x, (n-1)//2)



if __name__ == '__main__':
    init = Power()
    print(init.myPow(2.00000, 10))
    print(init.myPow(2.10000, 3))
    print(init.myPow(2.00000, -2))
