from typing import List


class JumpGame:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_index = 0
        for i in range(0, n):
            if max_index < i:
                return False
            max_index = max(max_index, nums[i] + i)
        return True


if __name__ == '__main__':
    init = JumpGame()
    print(init.canJump([2, 3, 1, 1, 4]))  # true
    print(init.canJump([3, 2, 1, 0, 4]))  # false
