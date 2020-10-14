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

        while nums[source]<nums[target]:
            source-=1






if __name__ == '__main__':
    init = NextPermutation()
    print(init.nextPermutation([1,2,4,3,1]))
