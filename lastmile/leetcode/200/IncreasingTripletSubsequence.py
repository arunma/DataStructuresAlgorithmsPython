from typing import List


class IncreasingTripletSubsequence:
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     ws = 0
    #     for we in range(1, len(nums)):
    #         if nums[we] > nums[we - 1]:
    #             if we-ws+1==3: return True
    #         else:
    #             ws=we
    #     return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


if __name__ == '__main__':
    init = IncreasingTripletSubsequence()
    print(init.increasingTriplet([1, 2, 3, 4, 5]))  # true
    print(init.increasingTriplet([5, 4, 3, 2, 1]))  # false
    print(init.increasingTriplet([5, 1, 5, 5, 2, 5, 4]))  # true
    print(init.increasingTriplet([2, 1, 5, 0, 4, 6]))  # true
    print(init.increasingTriplet([0, 4, 2, 1, 0, -1, -3]))  # false
    print(init.increasingTriplet([1,1,1,1,1,1]))  # false
