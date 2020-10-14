class FillInTheBlanks:
    def fillInTheBlanks(self, nums):
        for i, num in enumerate(nums):
            if not num:
                nums[i]=nums[i-1]
        return nums

if __name__ == '__main__':
    init = FillInTheBlanks()
    print(init.fillInTheBlanks([1,None,2,3,None,None,5,None]))
