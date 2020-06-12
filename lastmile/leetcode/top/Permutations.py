from typing import List


class Permutations:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = list()
        self.permuteInner(nums, 0, len(nums) - 1, result)
        return result

    def permuteInner(self, nums, left, right, result: List[List[int]]):
        if left == right:
            result.append(nums.copy())
        else:
            for i in range(left, right + 1):
                nums[i], nums[left] = nums[left], nums[i]
                self.permuteInner(nums, left + 1, right, result)
                nums[left], nums[i] = nums[i], nums[left]


if __name__ == '__main__':
    init = Permutations()
    print(init.permute([1, 2, 3]))
