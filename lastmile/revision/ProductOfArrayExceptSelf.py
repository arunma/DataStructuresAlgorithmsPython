from typing import List


class ProductOfArrayExceptSelf:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        lsum = [0] * N
        rsum = [0] * N
        lsum[0] = 1
        for i in range(1, N):
            lsum[i] = lsum[i - 1] * nums[i - 1]

        rsum[-1] = 1
        for i in reversed(range(N - 1)):
            rsum[i] = rsum[i + 1] * nums[i + 1]

        res = [0] * N
        for i in range(N):
            res[i] = lsum[i] * rsum[i]

        return res


if __name__ == '__main__':
    init = ProductOfArrayExceptSelf()
    print(init.productExceptSelf([1, 2, 3, 4]))
