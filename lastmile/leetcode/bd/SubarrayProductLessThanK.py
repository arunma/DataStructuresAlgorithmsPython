from typing import List


class SubarrayProductLessThanK:
    #contiguous subarrays
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ws=0
        result=0
        currprod=1
        for we, num in enumerate(nums):
            currprod*=num
            while ws<=we and currprod>=k:
                currprod/=nums[ws]
                ws+=1

            result=result if ws>we else result+(we-ws+1)
            currprod=1 if ws>we else currprod

        return result


if __name__ == '__main__':
    init = SubarrayProductLessThanK()
    print(init.numSubarrayProductLessThanK([10,5,2,6], 100))
