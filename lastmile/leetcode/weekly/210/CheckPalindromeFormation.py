class CheckPalindromeFormation:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalin(s):
            return s==s[::-1]

        if isPalin(a) or isPalin(b):
            return True

        N=len(a)
        left=0
        right=N-1

        while left<right:
            if a[left]!=b[right]:
                break
            left+=1
            right-=1

        return left!=0

if __name__ == '__main__':
    init = CheckPalindromeFormation()
    print(init.checkPalindromeFormation(a = "ulacfd", b = "jizalu"))#True
    print(init.checkPalindromeFormation(a = "abdef", b = "fecab"))#False
    print(init.checkPalindromeFormation(a = "cdeoo", b = "oooab")) #true
