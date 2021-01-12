from typing import List


class SortColors:
    def sortColors(self, nums: List[int]) -> None:
        zero=0
        one=0
        two=len(nums)-1

        while one<=two:
            if nums[one]==0:
                nums[zero], nums[one]=nums[one], nums[zero]
                zero+=1
                one+=1
            elif nums[one]==1:
                one+=1
            else:
                nums[one], nums[two]=nums[two], nums[one]
                two-=1



if __name__ == '__main__':
    init = SortColors()
