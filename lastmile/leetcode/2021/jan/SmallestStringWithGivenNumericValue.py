class SmallestStringWithGivenNumericValue:
    def getSmallestString(self, n: int, k: int) -> str:
        chars=['a']*n
        k-=n

        i=n-1
        while i>=0:
            nextCharPos=min(k, 25)
            nextChar=chr(ord(chars[i]) + nextCharPos)
            chars[i]=nextChar
            k-=nextCharPos
            i-=1
        return ''.join(chars)



if __name__ == '__main__':
    init = SmallestStringWithGivenNumericValue()
    print(init.getSmallestString(3, 27))
    print(init.getSmallestString(5, 73))
