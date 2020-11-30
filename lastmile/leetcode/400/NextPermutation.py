from typing import List


class NextPermutation:
    def nextPermutation(self, nums: List[int]) -> None:
        target=len(nums)-1
        while target>0 and nums[target-1]>=nums[target]:
            target-=1

        if target==0:
            nums.reverse()
            return

        target=target-1

        source=len(nums)-1
        while nums[source]<=nums[target]:
            source-=1

        nums[source], nums[target]=nums[target], nums[source]

        left=target+1
        right=len(nums)-1

        while left<=right:
            nums[left], nums[right]=nums[right], nums[left]
            left+=1
            right-=1






if __name__ == '__main__':
    init = NextPermutation()
    x=[1, 2, 4, 3, 1]
    init.nextPermutation(x) #[1,3,1,2,4]
    print(x)
    print(init.nextPermutation([1,2,3])) #[1,3,2]
