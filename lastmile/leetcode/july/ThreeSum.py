class ThreeSum:
    def threeSum(self, nums):
        nums.sort()
        result = set()
        for i in range(len(nums) - 1):
            self.twoSum(target=-nums[i], start=i + 1, end=(len(nums) - 1), nums=nums, result=result)
        return [list(each) for each in result]

    def twoSum(self, target, start, end, nums, result):
        while start < end:
            total = nums[start] + nums[end]
            if total == target:
                result.add(tuple([-target, nums[start], nums[end]]))
            if total < target:
                start += 1
            else:
                end -= 1


if __name__ == '__main__':
    init = ThreeSum()
    print(init.threeSum([-1, 0, 1, 2, -1, -4]))
