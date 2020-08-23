from typing import List


class Permutations:

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     self.permuteHelper(nums, result, 0, len(nums))
    #     return result
    #
    # def permuteHelper(self, nums, result, left, right):
    #     if left == right:
    #         result.append(nums.copy())
    #     else:
    #         for i in range(left, right):
    #             nums[i], nums[left] = nums[left], nums[i]
    #             self.permuteHelper(nums, result, left + 1, right)
    #             nums[left], nums[i] = nums[i], nums[left]

    def permute(self, nums):
        result = []
        self.permuteInner(nums, curr=[], result=result)
        return result

    def permuteInner(self, nums, curr, result):
        if not nums:
            result.append(curr.copy())
        for i in range(len(nums)):
            curr.append(nums[i])
            self.permuteInner(nums[0:i] + nums[i + 1:], curr, result)
            curr.pop()


# def permute(self, nums: List[int]) -> List[List[int]]:
#     result = []
#     self.permuteInner(nums, 0, len(nums) - 1, result)
#     return result
#
# def permuteInner(self, nums, left, right, result: List[List[int]]):
#     if left == right:
#         result.append(nums.copy())
#     else:
#         for i in range(left, right + 1):
#             nums[i], nums[left] = nums[left], nums[i]
#             self.permuteInner(nums, left + 1, right, result)
#             nums[left], nums[i] = nums[i], nums[left]


if __name__ == '__main__':
    init = Permutations()
    print(init.permute([1, 2, 3]))
