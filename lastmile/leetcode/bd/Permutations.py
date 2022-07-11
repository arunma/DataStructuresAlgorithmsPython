from typing import List


class Permutations:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.permInner(nums, 0, len(nums))
        return self.result

    def permInner(self, nums, start, end):
        if start == end:
            print("---->", nums.copy())
            self.result.append(nums.copy())
            return

        for i in range(start, end):
            print(f"i: {i}, s:{start}")
            # swap
            nums[start], nums[i] = nums[i], nums[start]
            self.permInner(nums, start + 1, end)
            # unswap
            nums[start], nums[i] = nums[i], nums[start]


if __name__ == '__main__':
    init = Permutations()
    print(init.permute([1,2,3]))
