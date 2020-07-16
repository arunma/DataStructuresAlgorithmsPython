from typing import List


class LargestDivisibleSubset:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []
        n = len(nums)
        nums.sort()
        sol = [[num] for num in nums]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(sol[i]) < len(sol[j]) + 1:
                        sol[i] = sol[i] + [nums[j]]
        return max(sol, key=len)


if __name__ == '__main__':
    init = LargestDivisibleSubset()
    print(init.largestDivisibleSubset([1, 2, 3]))
    print(init.largestDivisibleSubset([1, 2, 4, 8]))
