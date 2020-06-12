from typing import List


class SortColors:
    def sortColors(self, nums: List[int]) -> None:
        ostart=0
        oend=0
        left=0
        right=len(nums)-1

        while left<=right:
            if nums[left]==1:
                oend+=1
                left+=1
            elif nums[left]==0:
                nums[ostart], nums[left]=nums[left], nums[ostart]
                ostart+=1
                left+=1
            elif nums[left]==2:
                nums[right], nums[left] = nums[left], nums[right]
                right-=1



if __name__ == '__main__':
    init = SortColors()
    # l=[2,0,2,1,1,0]
    # init.sortColors(l)
    # print(l)

    l = [2, 0, 1]
    init.sortColors(l)
    print(l)

