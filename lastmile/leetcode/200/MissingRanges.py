from typing import List


class MissingRanges:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower - 1] + nums + [upper + 1]
        result = []
        for i in range(len(nums)):
            if nums[i] - nums[i - 1] == 2:
                result.append("{}".format(nums[i - 1] + 1))
            elif nums[i] - nums[i - 1] > 2:
                result.append("{}->{}".format(nums[i - 1] + 1, nums[i] - 1))
        return result


if __name__ == '__main__':
    init = MissingRanges()
    print(init.findMissingRanges([0, 1, 3, 50, 75], 0, 99))  # ["2", "4->49", "51->74", "76->99"]
    print(init.findMissingRanges([], 1, 1))  # ["2", "4->49", "51->74", "76->99"]
