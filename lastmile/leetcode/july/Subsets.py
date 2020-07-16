from typing import List


class Subsets:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     result=[]
    #     current=[]
    #     self.make_subsets(nums, result, current, 0)
    #     return result
    #
    # def make_subsets(self, nums, result, current, index):
    #     result.append(current[:])
    #
    #     for i in range(index, len(nums)):
    #         current.append(nums[i])
    #         self.make_subsets(nums, result, current, index+1)
    #         current.pop()
    #
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        current=[]
        result.append(current)
        for num in nums:
            for i in range(len(result)):
                cp = result[i].copy()
                cp.append(num)
                result.append(cp)
        return result



if __name__ == '__main__':
    init = Subsets()
    print(init.subsets([1,2,3]))
