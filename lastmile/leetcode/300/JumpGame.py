from typing import List


class JumpGame:
    def canJump(self, nums: List[int]) -> bool:
        maxReach=0

        for i,num in enumerate(nums):
            if i>maxReach:
                return False

            maxReach=max(i+num, maxReach)
        return True


if __name__ == '__main__':
    init = JumpGame()
    print(init.canJump(nums = [2,3,1,1,4])) #True
    print(init.canJump(nums = [3,2,1,0,4])) #False
