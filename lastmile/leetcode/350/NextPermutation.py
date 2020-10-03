from typing import List


class NextPermutation:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i==0:
            nums.reverse()
            return

        k = i - 1

        j = len(nums) - 1

        while nums[j] <= nums[k]:
            j -= 1

        nums[k], nums[j] = nums[j], nums[k]

        l = i
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1


if __name__ == '__main__':
    init = NextPermutation()
    #print(init.nextPermutation([1, 2, 3]))  # 1,3,2
    #print(init.nextPermutation([3, 2, 1]))  # 1,2,3
    #print(init.nextPermutation([1, 1, 5]))  # 1,5,1
    print(init.nextPermutation([1, 1]))  #
