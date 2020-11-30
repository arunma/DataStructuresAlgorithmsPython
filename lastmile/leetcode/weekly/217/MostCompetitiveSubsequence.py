import sys
from typing import List


class MostCompetitiveSubsequence:
    # def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
    #     self.result=nums
    #     self.helper(nums, k, 0, [])
    #     return self.result
    #
    # def helper(self, nums, k, start, curr):
    #     if len(curr)>k or start==len(nums):
    #         return
    #     if len(curr)==k and curr<self.result:
    #         self.result=curr
    #
    #     for i in range(start, len(nums)):
    #         self.helper(nums, k, i+1, curr+[nums[i]])

    # def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
    #     result = []
    #
    #     start = -1
    #     idx = 0
    #     start = -1
    #
    #     for i in range(k, 0, -1):
    #         mini = sys.maxsize
    #         for j in range(start + 1, len(nums) - i + 1):
    #             if nums[j] < mini:
    #                 start = j
    #                 mini = nums[j]
    #
    #         result.append(mini)
    #     return result


    def mostCompetitive(self, nums, k):
        stack=[]
        toRemove=len(nums)-k
        for i,num in enumerate(nums):
            while stack and num<stack[-1] and toRemove:
                toRemove-=1
                stack.pop()
            stack.append(num)

        while len(stack)>k:
            stack.pop()
        return stack


if __name__ == '__main__':
    init = MostCompetitiveSubsequence()
    print(init.mostCompetitive(nums=[3, 5, 2, 6], k=2))
    print(init.mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4))
    print(init.mostCompetitive(nums=[2, 4, 3, 7, 5, 4, 9, 6], k=4))
    # print(init.mostCompetitive(
    #     nums=[84, 10, 71, 23, 66, 61, 62, 64, 34, 41, 80, 25, 91, 43, 4, 75, 65, 13, 37, 41, 46, 90, 55, 8, 85, 61, 95,
    #           71], k=24))
