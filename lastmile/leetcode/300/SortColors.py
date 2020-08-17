from typing import List


class SortColors:
    def sortColors(self, nums: List[int]) -> None:
        ostart = 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == 0:
                nums[ostart], nums[left] = nums[left], nums[ostart]
                left += 1
                ostart += 1
            elif nums[left] == 1:
                left += 1
            else:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
        return nums


if __name__ == '__main__':
    init = SortColors()
    #print(init.sortColors([2, 0, 2, 1, 1, 0]))
    print(init.sortColors([2, 0, 1]))
