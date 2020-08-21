from typing import List


class MissingRanges:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        nums = [lower - 1] + nums + [upper + 1]

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 2:
                result.append("{}".format(nums[i] - 1))
            elif nums[i] - nums[i - 1] > 2:
                result.append("{}->{}".format(nums[i - 1] + 1, nums[i] - 1))
        return result


if __name__ == '__main__':
    init = MissingRanges()
    print(init.findMissingRanges(nums=[0, 1, 3, 50, 75], lower=0, upper=99))
    print(init.findMissingRanges(nums=[], lower=1, upper=1))
