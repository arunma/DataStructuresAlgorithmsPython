from typing import List


class ProductOfArrayExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left = [0] * N
        right = [0] * N
        left[0] = 1
        right[-1] = 1

        for l in range(1, N):
            left[l] = left[l - 1] * nums[l-1]

        for r in reversed(range(N - 1)):
            right[r] = right[r + 1] * nums[r + 1]

        prod = [0] * N
        for i in range(len(nums)):
            prod[i] = left[i] * right[i]

        return prod


if __name__ == '__main__':
    init = ProductOfArrayExceptSelf()
    print(init.productExceptSelf([1, 2, 3, 4]))
