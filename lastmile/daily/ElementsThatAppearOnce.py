class ElementsThatAppearOnce:

    def occurOnce(self, nums):
        xorOfAll=0
        for num in nums:
            xorOfAll^=num


        return xorOfAll


if __name__ == '__main__':
    init = ElementsThatAppearOnce()
    print(init.occurOnce([2, 4, 6, 8, 10, 2, 6, 10]))
    #print(init.occurOnce([2, 4, 6, 10, 2, 6, 10]))
