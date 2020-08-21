from typing import List

#NOT WORKING - NEED TO REVISIT
class WiggleSort:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort(reverse=True)
        half = len(nums[::2]) - 1
        left=nums[:half]
        right=nums[half:]
        print (left)
        print (right)
        nums.clear()
        while left or right:
            if left:
                nums.append(left.pop(0))
            if right:
                nums.append(right.pop(0))

if __name__ == '__main__':
    init = WiggleSort()
    #print(init.wiggleSort(list(range(1,8))))  # [1, 4, 1, 5, 1, 6].
    print(init.wiggleSort([1, 5, 1, 1, 6, 4]))  # [1, 4, 1, 5, 1, 6].
    print(init.wiggleSort([1, 3, 2, 2, 3, 1]))  # [2, 3, 1, 3, 1, 2].
