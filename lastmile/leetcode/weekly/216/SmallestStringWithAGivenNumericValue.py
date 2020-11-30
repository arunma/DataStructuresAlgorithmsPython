class SmallestStringWithAGivenNumericValue:
    # def getSmallestString(self, n: int, k: int) -> str:
    #     #for i, c in enumerate( 'abcdefghijklmnopqrstuvwxyz')
    #     alpha='abcdefghijklmnopqrstuvwxyz'
    #     self.result='z'*k
    #     self.helper(alpha, n, k, '', 0, {})
    #     return self.result
    #
    # def helper(self, alpha, n, k, curr, start, memo):
    #     if (n,k) in memo:
    #         return memo[(n,k)]
    #     else:
    #         if n==0 and k==0:
    #             self.result=min(self.result, curr, key=len)
    #             memo[(n, k)] = self.result
    #             return
    #         if n<0 or k<0:
    #             memo[(n, k)] = 'z'*k
    #             return
    #         for i in range(start, len(alpha)):
    #             alnum=ord(alpha[i])-96
    #             self.helper(alpha, n-1, k-alnum, curr+alpha[i], i, memo)
    #     memo[(n, k)] = 'z'*k

    def getSmallestString(self, n: int, k: int) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        zs='z'*((k-n)//25)
        ais='a'*(n-len(zs)-1)
        mids=alpha[(k-n)%25]
        return ais+mids+zs
        # z, rem = divmod(k-n, 25)
        # zs='z'*z
        # ayes='a'*(n-z-1)
        # mids=alpha[rem]
        #
        # return ayes+mids+zs




if __name__ == '__main__':
    init = SmallestStringWithAGivenNumericValue()
    print(init.getSmallestString(3,27))
    print(init.getSmallestString(3,28))
    print(init.getSmallestString(3,30))
    print(init.getSmallestString(5,73))
    print(init.getSmallestString(24,552))
    print(init.getSmallestString(85,2159))

    # aay
    # aaz
    # acz
    # aaszz
    # aadzzzzzzzzzzzzzzzzzzzzz
    # aayzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz