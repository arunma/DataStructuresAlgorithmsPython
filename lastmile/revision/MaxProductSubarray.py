import sys
from typing import List


class MaxProductSubarray:
    # def maxProduct(self, nums: List[int]) -> int:
    #     max_product=nums[0]
    #     res_product=-sys.maxsize
    #     for num in nums[1:]:
    #         max_product=max(num, max_product*num)
    #         res_product=max(max_product, res_product)
    #         print(f"Num: {num}, max product: {max_product}, res product: {res_product}")
    #     return res_product

    def maxProduct(self, nums: List[int]) -> int:
        max_product=nums[0]
        min_product=nums[0]
        res_product=-sys.maxsize
        for num in nums[1:]:
            temp_max=max(num, max_product*num, min_product*num)
            temp_min=min(num, max_product*num, min_product*num)

            max_product, min_product=temp_max, temp_min
            res_product=max(max_product, res_product)
            #print(f"Num: {num}, max product: {max_product}, min product: {min_product}, res product: {res_product}")
        return res_product


if __name__ == '__main__':
    init = MaxProductSubarray()
    #print(init.maxProduct([2, 3, 0, 4, 5]))
    print(init.maxProduct([2, 3, -2, 4]))  # 6
    print(init.maxProduct([-2, 0, -1]))  # 0
    # print(init.maxProduct([-2]))  # -2
    # print(init.maxProduct([0, 2]))  # 2
