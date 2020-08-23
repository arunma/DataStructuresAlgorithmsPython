from typing import List


class SubsetsII:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        curr = []
        self.helper(nums, curr, result, 0)
        return result

    def helper(self, nums, curr, result, start):
        result.append(curr.copy())
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:  # skip duplicates
                continue
            else:
                curr.append(nums[i])
                self.helper(nums, curr, result, i + 1)
                curr.pop()

    # def dfs(self, start, res, curr, nums):
    #     res.append(list(curr))
    #     for i in range(start, len(nums)):
    #         if i > start and nums[i] == nums[i - 1]:
    #             continue
    #         curr.append(nums[i])
    #         self.dfs(i + 1, res, curr, nums)
    #         curr.pop()
    #
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     res, path = [], []
    #     self.dfs(0, res, path, nums)
    #     #self.helper(nums, path, res, 0)
    #     return res

if __name__ == '__main__':
    init = SubsetsII()
    print(init.subsetsWithDup([1, 2, 2]))
