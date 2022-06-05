from typing import List


class ThreeSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N=len(nums)
        if N<3:
            return []
        nums.sort()
        result=set()
        for ti in range(N-2):
            self.twoSum(nums, -nums[ti], ti+1, N-1, result)
        return result

    def twoSum(self, nums, target, left, right, result):
        while left<right:
            csum=nums[left]+nums[right]
            if csum<target:
                left+=1
            elif csum>target:
                right-=1
            else:
                result.add((-target, nums[left], nums[right]))
                left+=1
                right-=1



if __name__ == '__main__':
    init = ThreeSum()
    print(init.threeSum([-1, 0, 1, 2, -1, -4]))
    print(init.threeSum([-1, 0, 1, -1]))
    '''
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    '''
