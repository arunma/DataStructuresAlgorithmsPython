from typing import List


class ProductOfArrayExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        result = []
        for i in range(len(left)):
            result.append(left[i] * right[i])

        return result


if __name__ == '__main__':
    init = ProductOfArrayExceptSelf()
    print(init.productExceptSelf([1, 2, 3, 4]))
