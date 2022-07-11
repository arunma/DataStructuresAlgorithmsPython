from typing import List


class ValidTriangleNumber:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)

        result = 0

        for k in range(2, N):
            low = 0
            high = k - 1

            while low < high:
                curr = nums[low] + nums[high]
                if curr > nums[k]:
                    result += high - low
                    high -= 1
                else:
                    low += 1
        return result


if __name__ == '__main__':
    init = ValidTriangleNumber()
    print(init.triangleNumber(nums = [2,2,3,4]))
