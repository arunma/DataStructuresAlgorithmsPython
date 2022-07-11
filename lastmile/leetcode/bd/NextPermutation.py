class NextPermutation:

    def nextPermutation(self, nums):
        N=len(nums)
        target=N-1

        while target>0 and nums[target-1]>=nums[target]:
            target-=1

        if target==0:
            nums.reverse()
            return nums

        target-=1

        source=N-1
        while nums[source]<=nums[target]:
            source-=1

        nums[source], nums[target]=nums[target], nums[source]

        left=target+1
        right=N-1

        while left<right:
            nums[left], nums[right]=nums[right], nums[left]
            left+=1
            right-=1

        return nums







if __name__ == '__main__':
    init = NextPermutation()
    #print(init.nextPermutation([1, 2, 4, 3, 1]))  # [1,3,1,2,4]
    #print(init.nextPermutation([1, 2, 3]))  # [1,3,2]
    #print(init.nextPermutation([1, 2]))  # [1,3,2]
    print(init.nextPermutation([1, 3, 2]))  # [2,1,3]
    print(init.nextPermutation([1, 5, 1]))  # [2,1,3]
