from typing import List


class MaximumConsecutiveOnesIII:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ws = 0
        ones = 0
        result = 0
        j = 0
        for we, num in enumerate(nums):
            if num == 1:
                ones += 1
            else:
                j += 1
                while j > k:
                    if nums[ws] == 0:
                        j -= 1
                    else:
                        ones-=1
                    ws += 1

            result = max(we - ws + 1, result)
        return result


if __name__ == '__main__':
    init = MaximumConsecutiveOnesIII()
    print(init.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k= 2)) #6
