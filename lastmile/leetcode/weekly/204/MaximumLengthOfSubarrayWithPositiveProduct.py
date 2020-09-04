from typing import List


class MaximumLengthOfSubarrayWithPositiveProduct:
#     def getMaxLen(self, nums: List[int]) -> int:
#         min_product=nums[0]
#         max_product=nums[0]
#         super_max=nums[0]
#         start=0
#         prevStart=0
#
#         for i in range(1, len(nums)):
#             curr_max=max(nums[i], min_product*nums[i], max_product*nums[i])
#             min_product=min(nums[i], min_product*nums[i], max_product*nums[i])
#
# #NOT sure
#             if curr_max<=max_product:
#                 start=i
#
#             max_product=curr_max
#
#             if super_max<=max_product:
#                 end=i-1
#                 super_max=max(max_product, super_max)
#         return end-start+1

    def getMaxLen(self, nums: List[int]) -> int:
        nums.append(0)

        start = 0
        ms = []
        to_ret = 0
        for i, t in enumerate(nums):
            if t == 0:
                if len(ms) % 2 == 0:
                    to_ret = max(to_ret, i - start)
                else:
                    to_ret = max([to_ret, i - ms[0] - 1, ms[-1] - start])
                start = i + 1
                ms = []
            elif t < 0:
                ms.append(i)
        return to_ret


if __name__ == '__main__':
    init = MaximumLengthOfSubarrayWithPositiveProduct()
    print(init.getMaxLen([1,-2,-3,4])) #4
