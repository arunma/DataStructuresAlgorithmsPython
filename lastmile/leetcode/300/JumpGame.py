from typing import List


class JumpGame:
    def canJump(self, nums: List[int]) -> bool:
        maxReach=0
        for i, num in enumerate(nums):
            if maxReach<i:
                return False
            maxReach=max(maxReach, i+num) #What is the maximum index you could reach
        return True


if __name__ == '__main__':
    init = JumpGame()
    print(init.canJump(nums = [2,3,1,1,4])) #True
    print(init.canJump(nums = [3,2,1,0,4])) #False
