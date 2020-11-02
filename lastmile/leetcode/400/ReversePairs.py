from typing import List


class ReversePairs:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.mergeAndCount(nums)
        return self.count

    def mergeAndCount(self, nums):
        if len(nums) <= 1:
            return nums

        left = self.mergeAndCount(nums[:len(nums) // 2])
        right = self.mergeAndCount(nums[len(nums) // 2:])

        l = r = 0
        while l < len(left) and r < len(right):
            if left[l] <= 2 * right[r]:
                l += 1
            else:
                self.count += len(left) - l
                r += 1

        return sorted(left + right)


if __name__ == '__main__':
    init = ReversePairs()
    print(init.reversePairs([1, 3, 2, 3, 1]))
